from flask import Flask, request, jsonify, Blueprint
from app import app
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