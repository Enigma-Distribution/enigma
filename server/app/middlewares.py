from flask import request, jsonify
from functools import wraps

from app import utils
from app.properties import get_site_secret_key

from traceback import print_exc


def get_decoded_token_from_header(request_header):
    if 'token' in request_header:
        obj = utils.get_object_from_token(request_header['token'], get_site_secret_key())
        return obj
        
def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            obj = get_decoded_token_from_header(request.headers)
            return f(obj['USER_ID'])
        except:
            print_exc()
            return jsonify({"STATUS": "FAIL", "MSG": "ERROR IN AUTHENTICATION"}), 401
    return decorated_function