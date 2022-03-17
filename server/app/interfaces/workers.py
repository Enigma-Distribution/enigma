from uuid import uuid4
from time import time
from hashlib import sha256

from psycopg2 import errors as pgerrors

from app.datastore import workers as workers_db
from app.validations import validate_secret
from app.exceptions import UsernameAlreadyExistsException, EmailAlreadyExistsException, PasswordMismatchException

def create_user(username, email, secret, upi_id):
    try:
        validate_secret(secret)
        user = {
            "worker_id": str(uuid4()),
            "username": username,
            "secret": sha256(secret.encode('utf-8')).hexdigest(),
            "email": email,
            "earning": 0,
            "upi_id": upi_id
        }
        workers_db.insert_user(user)
        return user
    except pgerrors.UniqueViolation:
        raise EmailAlreadyExistsException
    except pgerrors.UniqueViolation:
        raise UsernameAlreadyExistsException

def get_username_from_email_password(email, secret):
    secret = sha256(secret.encode('utf-8')).hexdigest()
    data = workers_db.select_user_id_from_email_pass(email, secret)
    if data and len(data) > 0:
        return data
    raise PasswordMismatchException