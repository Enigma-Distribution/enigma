from uuid import uuid4
from time import time
from hashlib import sha256

from psycopg2 import errors as pgerrors

from app.datastore import users as users_db
from app.validations import validate_secret
from app.exceptions import EmailAlreadyExistsException, PasswordMismatchException


def create_user(name, email, secret):
    try:
        validate_secret(secret)
        user = {
            "username": str(uuid4()),
            "name": name,
            "date_added": str(int(time())),
            "secret": sha256(secret.encode('utf-8')).hexdigest(),
            "email": email
        }
        users_db.insert_organization(user)
        user['total_tasks'] = 0
        return user
    except pgerrors.UniqueViolation:
        raise EmailAlreadyExistsException


def get_username_from_email_password(email, secret):
    secret = sha256(secret.encode('utf-8')).hexdigest()
    data = users_db.select_org_id_from_email_pass(email, secret)
    if data and len(data) > 0:
        return data[0]
    raise PasswordMismatchException
