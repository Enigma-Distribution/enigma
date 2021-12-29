from flask import Blueprint
from flask import Flask, request, jsonify
from app import app
from app.properties import get_aws_access_key_id, get_aws_secret_access_key, get_aws_session_token, get_s3_bucket_name
from app.exceptions import EnigmaException
from werkzeug.utils import secure_filename
import boto3
import uuid
from app.constants import SERVER_ERROR

s3 = boto3.client("s3",
                    aws_access_key_id = get_aws_access_key_id(),
                    aws_secret_access_key = get_aws_secret_access_key(),
                    aws_session_token = get_aws_session_token()
                     )
uploads = Blueprint('uploads', __name__)

@uploads.route("/upload-file")
def upload_file():
    try:
        file = request.files['file']
        if file:
            filename = uuid.uuid4()
            file.save(filename)
            s3.upload_file(
                Bucket = get_s3_bucket_name(),
                Filename = filename,
                Key = filename
            )
        return jsonify({"STATUS": "OK", "file_id": filename})
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
