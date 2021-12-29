from uuid import uuid4
from time import time
from hashlib import sha256

from psycopg2 import errors as pgerrors

from app.datastore import users as users_db
from app.validations import validate_secret
from app.exceptions import UsernameAlreadyExistsException, EmailAlreadyExistsException, PasswordMismatchException


def create_user(username, email, secret):
    try:
        validate_secret(secret)
        user = {
            "user_id": str(uuid4()),
            "username": username,
            "date_added": str(int(time())),
            "secret": sha256(secret.encode('utf-8')).hexdigest(),
            "email": email
        }
        users_db.insert_user(user)
        user['total_tasks'] = 0
        return user
    except pgerrors.UniqueViolation:
        raise EmailAlreadyExistsException
    except pgerrors.UniqueViolation:
        raise UsernameAlreadyExistsException

def get_username_from_email_password(email, secret):
    secret = sha256(secret.encode('utf-8')).hexdigest()
    data = users_db.select_org_id_from_email_pass(email, secret)
    if data and len(data) > 0:
        return data
    raise PasswordMismatchException
