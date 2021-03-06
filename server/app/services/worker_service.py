from flask import Flask, request, jsonify, Blueprint
# from app import app
from app.interfaces import steps as step_service
from app.interfaces import tasks as task_service
from app.interfaces import workers as worker_service
from app.interfaces import transactions as transaction_service
from app.exceptions import EnigmaException
from app.middlewares import user_required
from app.utils import read_file_content, put_content_into_file_and_upload
from werkzeug.utils import secure_filename
from app.constants import SERVER_ERROR
import json
import pytz
from datetime import datetime  

app = Blueprint("worker_service", __name__)
phase_identifier = 0

@app.route('/worker/allot-me', methods=['POST'])
@user_required
def allot_step(worker_id):
    global phase_identifier
    try:
        counter = 0
        print(phase_identifier)
        while counter<3:
            if phase_identifier == 0:
                # allot map phase step
                print("map")
                step = step_service.get_step_to_allot("map")
                if step == None:
                    phase_identifier+=1
                else:
                    break

            if phase_identifier == 1:
                # allot shuffle phase step
                print("shuffle")
                step = step_service.get_step_to_allot("shuffle")
                if step == None:
                    phase_identifier+=1
                else:
                    break

            if phase_identifier == 2:
                # allot reduce phase step
                print("reduce")
                step = step_service.get_step_to_allot("reduce")             
                if step:
                    break

            phase_identifier+=1
            phase_identifier = phase_identifier%3
            counter+=1
        
        available = True
        if counter == 3:
            available = False
        print("step before assignment")
        print(step)
        
        if available == True:
            step_service.assign_step_to_worker(worker_id, step[0]["step_id"])

        return jsonify({"STATUS": "OK", "AVAILABLE": available, "STEP": step})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501

# {
#     "step_id":"f815df08-dd9f-4e73-ad1f-c974f39abbc1",
#     "phase":"map",
#     "result_file_id":"rugved"
# }

@app.route('/worker/submit-result', methods=['POST'])
@user_required
def get_result(worker_id):
    print("worker_id",worker_id)
    # return jsonify({"STATUS": "TEST","worker_id":worker_id})
    try:
        if request.get_json():
            print("request.form is none")
            data =  request.get_json()
            transaction_type = data["transaction_type"]
            step_id = data["step_id"]
            result_file_id = data["result_file_id"] 
        else:
            print("request.form is NOT none")
            data =  request.form
            transaction_type = data.get("transaction_type", "REGULAR")
            step_id = data.get("step_id")
            result_file_id = data.get("result_file_id") 

        print("incoming request data")
        print(data)

        step_data = step_service.get_step_by_step_id(step_id)
        print("step_data",step_data)

        if step_data == None:
            return jsonify({"STATUS": "FAIL", "MSG": "No such step exist. Step_id: " + step_id})
        
        if step_data["assigned_to"] != worker_id:
            return jsonify({"STATUS": "FAIL", "MSG": "CURRENTLY, THE STEP " + step_id  + " IS NOT ALLOTED TO YOU"})

        phase = step_data["phase"]
        step_ts_after_allotment = step_data['step_updated_ts']
        tz_NY = pytz.timezone('Asia/Kolkata')
        ts_after_completion_of_step = datetime.now(tz_NY)
        efficiency = ((ts_after_completion_of_step - step_ts_after_allotment).total_seconds())/60

        amount = 1
        
        
        # validate result here. If result is not valid i.e there is some error in result sent by worker, handle it (reassign)
        
        # As result is valid, make a transaction
        transaction_data = {
            "transaction_type": transaction_type, #data.get("transaction_type", "REGULAR"), 
            "amount": amount,
            "worker_id": worker_id,
            "step_id": step_id, 
            "phase": phase,
            "result_file_id": result_file_id, #data.get("result_file_id"),
            "efficiency": efficiency
        }

        try:
            transaction_service.insert_transaction(transaction_data)
        except Exception as e:
            print("Transaction creating failed")

        # return jsonify({"STATUS": "TEST till transaction","worker_id":worker_id})

        # if completed phase is map update step with shuffle phase
        if phase == "map":
            print("inside map phase")
            task_id = step_service.update_completed_step("shuffle", result_file_id, step_id)[0]
            print(task_id)
        elif phase == "shuffle":
            print("inside shuffle phase")
            task_id = step_service.update_completed_step("reduce", result_file_id, step_id)[0]
            print(task_id)
        elif phase == "reduce":
            print("inside reduce phase")
            print("---------> step_id",step_id)
            task_id = step_service.update_completed_reduce_step("COMPLETED", result_file_id, step_id)[0]
            print("---------> task_id")
            print(task_id)

            
            # check if all steps in reduce phase and complete -> then aggregate result
            task_status = step_service.is_task_completed(step_id)
            print("Received task status", task_status)
            if task_status == True:
                print("---------- RESULT AGGREGATOR ----------")
                # api call to aggregate results 
                # 1) get all the steps of this "task". ALl steps should have completed reduce phase
                steps = step_service.get_all_steps(task_id)
                print("----------> Received all steps after completion")
                print("Count",len(steps))
                # 2) Read the result files ids of all steps.
                steps_result_files_cids = []
                for step in steps:
                    print(step['step_id'], step['result_file_id'])
                    steps_result_files_cids.append(step['result_file_id'])
                print("----------> steps_result_files_cids")
                print(steps_result_files_cids)

                list_of_result_dicts = []
                for cid in steps_result_files_cids:
                    # for testing hardcoding cid (Comment the below 1 line before pushing)
                    # cid = "QmPWfMrZijFSR5B9Q36Wy1nJ33JdGU6eitjnLETLQjLsAL"
                    file_link = "https://ipfs.infura.io/ipfs/" + cid
                    content = read_file_content(file_link)
                    d = json.loads(content)
                    list_of_result_dicts.append(d)
                
                print("---------> list_of_result_dicts")
                print(list_of_result_dicts)

                # 3) It will contain dictionaries. Merge them.
                final_result_dict = {}
                for d in list_of_result_dicts:
                    for key, value in d.items():
                        final_result_dict[key] = final_result_dict.get(key, 0) + value
                
                print("-----> final_result_dict")
                print(final_result_dict)

                # 4) Put this result on ipfs and modify task's "result_file_id" field
                final_result_dict = json.dumps(final_result_dict)
                result_file_id = put_content_into_file_and_upload(final_result_dict)
                print("FINAL result_file_id", result_file_id)
                # Example FINAL result_file_id -> QmWSRT5gUnQg1STmVyEq2u8xavQPVVJz3eZQDsWRkzaV1c
                
                # 5) Update in database
                print("Updating result for ",task_id)
                # result_file_id = 'QmWSRT5gUnQg1STmVyEq2u8xavQPVVJz3eZQDsWRkzaV1c'
                task_service.update_completed_task(task_id, result_file_id)

                # 6) Send user a notification/mail etc    
                pass
            else:
                print("Not all steps of task", task_id, "have been completed so did not call RESULT AGGREGATOR")
        return jsonify({"STATUS": "OK"})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501