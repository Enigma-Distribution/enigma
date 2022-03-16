from flask import Flask, request, jsonify, Blueprint
from app import app
from app.interfaces import tasks as task_service
from app.interfaces import steps as step_service
from app.exceptions import EnigmaException
from app.middlewares import user_required
from werkzeug.utils import secure_filename
from app.constants import SERVER_ERROR

app = Blueprint("task_service", __name__)

@app.route('/alltasks', methods=['POST'])
@user_required
def alltasks(current_user):
    try:
        data = task_service.get_all_tasks(current_user)
        return jsonify({"STATUS": "OK", "DATA": data})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": e}), 501

@app.route('/newtask', methods=['POST'])
@user_required
def newtask(current_user):
    try:
        data = request.form
        # user_id = current_user.user_id
        task_name = data.get('task_name')
        task_description = data.get('task_description')
        task_zip_file_id = data.get('task_zip_file_id') 
        datasource_size = data.get('datasource_size')
        task_status = False
        task = task_service.create_task(current_user, task_name, task_description, task_zip_file_id, datasource_size, task_status)
        
        # Array of step_cid, step_size 
        all_steps = data.get('datasource_all_cids')
        #Create Steps -> Add to db
        for step_instance in all_steps:
            step = step_service.create_step(task.task_id, step_instance.step_cid, "map", None, False, None, step_instance.step_size)
        
        #Add Steps to Queue -> RabbitMQ
        
        return jsonify({"STATUS": "OK", "TASK": task})
    except Exception as e:
        # return jsonify({"alert": "Error!"})
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/task', methods=['POST'])
@user_required
def taskdetails(current_user):
    try:
        task_id = request.args['task_id']
        task = task_service.get_selected_task(task_id, current_user)
        return jsonify({"STATUS": "OK", "TASK": task})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501