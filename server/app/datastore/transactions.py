from app.properties import get_pg_connection

QUERY_INSERT_TRANSACTION = "INSERT INTO transaction(transaction_id, transaction_type, amount, worker_id, step_id, phase, result_file_id, efficiency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

db = get_pg_connection()

def insert_transaction(data):
    values = (data['transaction_id'], data['transaction_type'], data['amount'], data['worker_id'], data['step_id'], data['phase'], data['result_file_id'], data['efficiency'])
    
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_TRANSACTION, values)