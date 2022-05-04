from flask import Flask, request, jsonify, Blueprint
# from app import app
from app.interfaces import steps as step_service
from app.exceptions import EnigmaException
from app.middlewares import user_required
from werkzeug.utils import secure_filename
from app.constants import SERVER_ERROR

app = Blueprint("step_service", __name__)

@app.route('/task/create_step', methods=['POST'])
@user_required
def newtask(current_user):
    try:
        data = request.form
        task_id = data.get('task_id')
        datasource_id = data.get('datasource_id')
        phase = data.get('phase')
        assigned_to = data.get('assigned_to')
        is_completed = data.get('is_completed')
        result_file_id = data.get('result_file_id')
        step_size = data.get('step_size')
        step = step_service.create_step(task_id, datasource_id, phase, assigned_to, is_completed, result_file_id, step_size)

        return jsonify({"STATUS": "OK", "STEP": step})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/task/get_task_meta_data', methods=['POST'])
@user_required
def get_task_meta_data(current_user):
    try:
        task_id = request.args['task_id']
        steps = step_service.get_all_steps(task_id)
        count_completed_steps = 0
        count_steps_in_map_phase = 0
        count_steps_in_shuffle_phase = 0
        count_steps_in_reduce_phase = 0
        for step in steps:
            if step['is_completed'] == 1:
                count_completed_steps+=1
            if step['phase'] == "map":
                count_steps_in_map_phase+=1
            if step['phase'] == "shuffle":
                count_steps_in_shuffle_phase+=1
            if step['phase'] == "reduce" and step['is_completed'] == 0:
                count_steps_in_reduce_phase+=1
        total_steps = len(steps)

        counts = {
            "total_steps": total_steps,
            "count_completed_steps": count_completed_steps,
            "count_steps_in_map_phase": count_steps_in_map_phase,
            "count_steps_in_shuffle_phase": count_steps_in_shuffle_phase,
            "count_steps_in_reduce_phase": count_steps_in_reduce_phase
        }

        return jsonify({"STATUS": "OK", "COUNTS": counts, "STEPS": steps})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501