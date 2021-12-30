from flask import Blueprint
from flask import Flask, request, jsonify
from app import app
from app.properties import get_s3_bucket
from app.exceptions import EnigmaException
from werkzeug.utils import secure_filename
import uuid
from app.constants import SERVER_ERROR

uploads = Blueprint('uploads', __name__)

@uploads.route("/upload-file", methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        if file:
            file_id = uuid.uuid4()
            s3_bucket_instance = get_s3_bucket()
            s3_bucket_instance.put_object(
                Key=file_id,
                Body=file,
                ACL='public-read'
            )
        return jsonify({"STATUS": "OK", "file_id": file_id})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

# s3.meta.client.download_file('BUCKET_NAME', 'FILENAME.txt', '/TASKID/FILENAME.txt')

# NOT REQUIRED
# @uploads.route("/get-file")
# def get_file():
#     try:
#         return jsonify({"STATUS": "OK", "file_link": "dummy-link"})
#     except Exception as e:
#         return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501
