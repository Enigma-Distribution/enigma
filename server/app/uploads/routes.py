from flask import Blueprint
from flask import Flask, request, jsonify
# from app import app
from app.properties import get_s3_bucket
from app.exceptions import EnigmaException
from werkzeug.utils import secure_filename
import uuid
from app.constants import SERVER_ERROR

uploads = Blueprint('uploads', __name__)

@uploads.route("/upload-file", methods=['POST'])
def upload_file():
    print("Upload Filess!!")
    try:
        file = request.files['file']
        task_file = request.form.get("task_file")
        if file:
            file_id = str(uuid.uuid4())
            if task_file == True:
                file_id = "Task-" + str(file_id)
            filename = secure_filename(file_id)
            s3_bucket_instance = get_s3_bucket()
            s3_bucket_instance.put_object(
                Body=file,
                Key=file_id,
                ACL='public-read'
            )
        return jsonify({"STATUS": "OK", "file_id": file_id})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)}), 501

# s3.meta.client.download_file('BUCKET_NAME', 'FILENAME.txt', '/TASKID/FILENAME.txt')

# NOT REQUIRED
# @uploads.route("/get-file")
# def get_file():
#     try:
#         return jsonify({"STATUS": "OK", "file_link": "dummy-link"})
#     except Exception as e:
#         return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501
