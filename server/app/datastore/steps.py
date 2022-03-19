from app.properties import get_pg_connection

QUERY_INSERT_STEP = "INSERT INTO step(step_id, task_id, datasource_id, phase, assigned_to, is_completed, result_file_id, step_size) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

QUERY_UPDATE_COMPLETED_STEP = "UPDATE step SET phase = %s, datasource_id = %s, assigned_to = %s, step_updated_ts = %s WHERE step_id = %s"

QUERY_UPDATE_COMPLETED_REDUCE_STEP = "UPDATE step SET is_completed = %s, step_updated_ts = %s WHERE step_id = %s"

QUERY_GET_TASK_ID = "SELECT task_id FROM step WHERE step_id = %s"

QUERY_GET_STEPS_UNFINISHED = "SELECT step_id FROM step WHERE task_id = %s AND is_completed = %s ORDER BY step_updated_ts ASC"

QUERY_FETCH_STEPS = "SELECT * FROM step WHERE task_id = %s"

QUERY_GET_STEP_TO_ALLOT_FROM_QUEUE = "SELECT step_id, task_id, phase, datasource_id FROM step WHERE phase = %s ORDER BY step_updated_ts ASC LIMIT 1 "

db = get_pg_connection()

def insert_step(step):
    values = (step['step_id'], step['task_id'], step['datasource_id'], step['phase'], step['assigned_to'], step['is_completed'], step['result_file_id'], step['step_size'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_STEP, values)

def update_completed_step(step):
    values = (step['phase'], step['datasource_id'], None, step['step_id'], step['step_updated_ts'], )
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_UPDATE_COMPLETED_STEP, values)

def update_completed_reduce_step(step):
    values = (step['is_completed'], step['step_id'], step['step_updated_ts'], )
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_UPDATE_COMPLETED_REDUCE_STEP, values)

def get_task_id(step_id):
    values = (step_id)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_TASK_ID, values)
            return cursor.fetchone()

def get_steps_unfinished_in_reduce_phase(task_id):
    values = (task_id, 0)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_STEPS_UNFINISHED, values)
            return cursor.fetchall()

def select_all_steps_for_task_id(task_id):
    values = (task_id,)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_FETCH_STEPS, values)
            return cursor.fetchall()

def get_step_to_allot(step_phase):
    values = (step_phase,)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_STEP_TO_ALLOT_FROM_QUEUE, values)
            return cursor.fetchone()
