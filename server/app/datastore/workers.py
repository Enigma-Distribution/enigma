from app.properties import get_pg_connection

QUERY_INSERT_USER = "INSERT INTO worker(worker_id , username, password_hash, email, earnings, upi_id) VALUES (%s, %s, %s, %s, %s, %s)"

QUERY_SELECT_USERNAME_FROM_EMAIL_PASS = "SELECT worker_id, username FROM worker WHERE email = %s AND password_hash = %s"

QUERY_INSERT_TRANSACTION = "INSERT INTO transaction(transaction_id, transaction_type, amount, worker_id, step_id, phase, result_file_id, efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

db = get_pg_connection()

def insert_user(user):
    values = (user['worker_id'], user['username'], user['secret'], user['email'], user['earnings'], user['upi_id'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_USER, values) 

def select_user_id_from_email_pass(email, secret):
    values = (email, secret)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_SELECT_USERNAME_FROM_EMAIL_PASS, values)
            return cursor.fetchone()

def insert_transaction(data):
    values = (data['transaction_id'], data['transaction_type'], data['amount'], data['worker_id'], data['step_id'], data['phase'], data['result_file_id'], data['efficiency'])
    
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_TRANSACTION, values)