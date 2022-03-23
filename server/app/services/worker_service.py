from flask import Flask, request, jsonify, Blueprint
from app import app
from app.interfaces import steps as step_service
from app.exceptions import EnigmaException
from app.middlewares import user_required
from werkzeug.utils import secure_filename
from app.constants import SERVER_ERROR

app = Blueprint("worker_service", __name__)
phase_identifier = 0

@app.route('/worker/allot-me', methods=['POST'])
@user_required
def allot_step(current_user):
    global phase_identifier
    try:
        counter = 0
        while counter<3:
            if phase_identifier == 0:
                # allot map phase step
                step = step_service.get_step_to_allot("map")
                if step == None:
                    phase_identifier+=1
                else:
                    break

            if phase_identifier == 1:
                # allot shuffle phase step
                step = step_service.get_step_to_allot("shuffle")
                if step == None:
                    phase_identifier+=1
                else:
                    break

            if phase_identifier == 2:
                # allot reduce phase step
                step = step_service.get_step_to_allot("reduce")             
                if step:
                    break

            phase_identifier+=1
            phase_identifier = phase_identifier%3
            counter+=1
        
        available = True
        if counter == 3:
            available = False

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
def get_result(current_user):
    try:
        data = request.form
        step_id = data.get("step_id")
        phase = data.get("phase")
        print(phase)
        result_file_id = data.get("result_file_id")  
        # id completed phase is map update step with shuffle phase
        if phase == "map":
            print("inside map phase")
            task = step_service.update_completed_step("shuffle", result_file_id, step_id)
        elif phase == "shuffle":
            task = step_service.update_completed_step("reduce", result_file_id, step_id)
        elif phase == "reduce":
            task = step_service.update_completed_reduce_step(step_id)
            # check if all steps in reduce phase and complete -> then aggregate result
            task_status = step_service.is_task_completed(step_id)
            if task_status == True:
                # api call to aggregate results 
                pass

        return jsonify({"STATUS": "OK"})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501