from app.properties import get_pg_connection

QUERY_INSERT_USER = "INSERT INTO users(user_id, username, date_added, secret_key, email) VALUES (%s, %s, %s, %s, %s)"

QUERY_SELECT_USERNAME_FROM_EMAIL_PASS = "SELECT user_id, username FROM users WHERE email = %s AND secret_key = %s"

db = get_pg_connection()

def insert_user(user):
    values = (user['user_id'], user['username'], user['date_added'], user['secret'], user['email'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_USER, values)

def select_org_id_from_email_pass(email, secret):
    values = (email, secret)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_SELECT_USERNAME_FROM_EMAIL_PASS, values)
            return cursor.fetchone()