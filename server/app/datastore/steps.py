from app.properties import get_pg_connection

QUERY_INSERT_STEP = "INSERT INTO step(step_id, task_id, datasource_id, phase, assigned_to, is_completed, result_file_id, step_size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

QUERY_UPDATE_STEP = ""

QUERY_FETCH_STEPS = "SELECT * FROM step WHERE task_id = %s"

db = get_pg_connection()

def insert_step(step):
    values = (step['step_id'], step['task_id'], step['datasource_id'], step['phase'], step['assigned_to'], step['is_completed'], step['result_file_id'], step['step_size'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_STEP, values)

def select_all_steps_for_task_id(task_id):
    values = (task_id,)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_FETCH_STEPS, values)
            return cursor.fetchall()