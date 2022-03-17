from flask import Flask, request, jsonify, Blueprint
from app import app
from app.interfaces import steps as step_service
from app.exceptions import EnigmaException
from app.middlewares import user_required
from werkzeug.utils import secure_filename
from app.constants import SERVER_ERROR

app = Blueprint("worker_service", __name__)

@app.route('/worker/allot-me', methods=['POST'])
@user_required
def allot_step(current_user):
    try:
        pass
        # Allot a step to user with following details

        # "STEP": {
        #     "step_id":"id",
        #     "phase":"phase",
        #     "zip_file_url":"url",
        #     "data_source_url":"url"
        # }

        return jsonify({"STATUS": "OK", "STEP": step})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501


@app.route('/worker/submit-result', methods=['POST'])
@user_required
def get_result(current_user):
    try:
        data = request.form
        step_id = data.get("step_id")
        phase = data.get("phase")
        result_file_id = data.get("result_file_id")  
        # id completed phase is map update step with shuffle phase
        if phase == "map":
            task = step_service.update_completed_step("shuffle", result_file_id, step_id)
        elif phase == "shuffle":
            task = step_service.update_completed_step("reduce", result_file_id, step_id)
        elif phase == "reduce":
            task = step_service.update_completed_reduce_step()
            # check if all steps in reduce phase and complete -> then aggregate result
            task_status = step_service.is_task_completed(step_id)
            if task_status == True:
                # api call to aggregate results 
                pass
        return jsonify({"STATUS": "OK", "STEP": step})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501