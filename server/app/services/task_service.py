from flask import Flask, request, jsonify
from app import app
from app.interfaces import tasks as task_service
from app.properties import get_aws_access_key_id, get_aws_secret_access_key, get_aws_session_token, get_s3_bucket_name
from app.exceptions import EnigmaException
from werkzeug.utils import secure_filename
import boto3
from app.constants import SERVER_ERROR

s3 = boto3.client('s3',
                    aws_access_key_id = get_aws_access_key_id(),
                    aws_secret_access_key = get_aws_secret_access_key(),
                    aws_session_token = get_aws_session_token()
                     )

@app.route('/alltasks', methods=['POST'])
def alltasks(current_user):
    try:
        data = task_service.get_all_tasks(current_user)
        return jsonify({"STATUS": "OK", "DATA": data})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/newtask', methods=['POST'])
def newtask(current_user):
    try:
        mapfile = request.files['mapfile']
        if mapfile:
            filename = secure_filename(mapfile.filename)
            mapfile.save(filename)
            s3.upload_file(
                Bucket = get_s3_bucket_name(),
                Filename=filename,
                Key = filename
            )

        reducefile = request.files['reducefile']
        if reducefile:
            filename = secure_filename(reducefile.filename)
            reducefile.save(filename)
            s3.upload_file(
                Bucket = get_s3_bucket_name(),
                Filename=filename,
                Key = filename
            )
            # msg = "Upload Done!"
        data = request.get_json()
        user = current_user
        name = data['name']
        mapfile_id = data['mapfile_id']
        reducefile_id = data['reducefile_id']
        data_source = data['data_source']
        status = data['status']
        task = task_service.create_task(user, name, mapfile_id, reducefile_id, data_source, status)
        return jsonify({"STATUS": "OK", "TASK": task})
    except Exception as e:
        return jsonify({"alert": "Error!"})
    return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/task')
def taskdetails(current_user):
    try:
        task_id = request.args['taskid']
        task = task_service.get_selected_task(task_id, current_user)
        return jsonify({"STATUS": "OK", "TASK": task})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501