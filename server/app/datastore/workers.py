from app.properties import get_pg_connection

QUERY_INSERT_USER = "INSERT INTO worker(worker_id , username, password_hash, email, earnings, upi_id) VALUES (%s, %s, %s, %s, %s, %s)"

QUERY_SELECT_USERNAME_FROM_EMAIL_PASS = "SELECT worker_id, username FROM worker WHERE email = %s AND password_hash = %s"

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