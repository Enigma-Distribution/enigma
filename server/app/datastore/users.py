from app.properties import get_pg_connection

QUERY_INSERT_USER = "INSERT INTO enigma_user(user_id, username, password_hash, email) VALUES (%s, %s, %s, %s)"

QUERY_SELECT_USERNAME_FROM_EMAIL_PASS = "SELECT user_id, username FROM enigma_user WHERE email = %s AND password_hash = %s"

db = get_pg_connection()

def insert_user(user):
    values = (user['user_id'], user['username'], user['secret'], user['email'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_USER, values)

def select_user_id_from_email_pass(email, secret):
    values = (email, secret)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_SELECT_USERNAME_FROM_EMAIL_PASS, values)
            return cursor.fetchone()