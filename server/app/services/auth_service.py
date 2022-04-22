from flask import Flask, request, jsonify, Blueprint
# from app import app

from app.interfaces import users as auth_service
from app.interfaces import workers as worker_auth_service
from app.middlewares import user_required
from app.exceptions import EnigmaException
from app.utils import get_object_from_token, get_token_from_object
from app.properties import get_site_secret_key
from app.constants import SERVER_ERROR, INCOMPLETE_DATA

app = Blueprint("auth_service", __name__)

@app.route('/auth/verify', methods=['POST'])
def authenticate_token():
    try:
        data = request.get_json()
        token = data['token']
        if get_object_from_token(token, get_site_secret_key()):
            return jsonify({"STATUS": "OK"})
        return jsonify({"STATUS": "FAIL", "MSG": "Invalid Token."})
    except KeyError as e:
        return jsonify({"STATUS": "FAIL", "MSG": INCOMPLETE_DATA + str(e)})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/authenticate/user', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        user_type = data['user_type']
        email = data['email']
        password = data['password']
        
        if user_type == "user":
            data = auth_service.get_username_from_email_password(email, password)
        elif user_type == "worker":
            data = worker_auth_service.get_username_from_email_password(email, password)

        token_contents = {
            "USER_ID": data[0]
        }
        token = get_token_from_object(token_contents, get_site_secret_key(), 7200)
        username = data[1]
        return jsonify({"STATUS": "OK", "TOKEN": token, "USERNAME": username, "EMAIL": email})
    except KeyError as e:
        return jsonify({"STATUS": "FAIL", "MSG": INCOMPLETE_DATA + str(e)})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/authentication/tokens/create', methods=['POST'])
@user_required
def create_access_token(user_id):
    try:
        data = request.get_json()
        access_rights = data['access_rights']
        task_id = data['task_id']
        valid_till = data['valid_till']
        token_contents = {
            "ACCESS_RIGHTS": access_rights,
            "TASK_ID": task_id,
            "USER_ID": user_id
        }
        if valid_till == "-":
            valid_till = None
        token = get_token_from_object(token_contents, get_site_secret_key(), valid_till)
        return jsonify({"STATUS": "OK", "TOKEN": token})
    except KeyError as e:
        return jsonify({"STATUS": "FAIL", "MSG": INCOMPLETE_DATA + str(e)})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": SERVER_ERROR}), 501

@app.route('/authenticate/user/new', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_type = data['user_type']
        email = data['email']
        password = data['password']
        username = data['username']
        token_contents = {}
        if user_type == "user":
            user = auth_service.create_user(username, email, password)
            token_contents = {
                    "USER_ID": user['user_id']
                }
        elif user_type == "worker":
            upi_id = data["upi_id"]
            user = worker_auth_service.create_worker(username, email, password, upi_id)
            token_contents = {
                    "USER_ID": user['worker_id']
                }
        token = get_token_from_object(token_contents, get_site_secret_key(), 7200)
        username = user['username']
        return jsonify({"STATUS": "OK", "TOKEN": token, "USERNAME": username, "EMAIL": email})
    except KeyError as e:
        return jsonify({"STATUS": "FAIL", "MSG": INCOMPLETE_DATA + str(e)})
    except EnigmaException as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)})
    except Exception as e:
        return jsonify({"STATUS": "FAIL", "MSG": str(e)}), 501
