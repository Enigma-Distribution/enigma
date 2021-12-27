from app.properties import get_pg_connection

QUERY_INSERT_TASK = "INSERT INTO tasks(task_id, user, date_created, name, mapfile_id, reducefile_id, data_source, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

QUERY_GET_ALL_TASKS = "SELECT task_id, name, date_created, mapfile_id, reducefile_id, data_source, status FROM tasks WHERE user = %s ORDER BY created_ts DESC"

QUERY_GET_SPECIFIC_TASK = "SELECT task_id, name, date_created, mapfile_id, reducefile_id, data_source, status FROM tasks WHERE task_id = %s AND user = %s"

db = get_pg_connection()

def insert_task(task, user):
    values = (task['task_id'], user, task['date_created'], task['name'], task['mapfile_id'], task['reducefile_id'], task['data_source'], task['status'])
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_INSERT_TASK, values)

def select_all_tasks(user):
    values = (user,)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_ALL_TASKS, values)
            return cursor.fetchall()

def select_specific_task(task_id, user):
    values = (task_id, user)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_SPECIFIC_TASK, values)
            return cursor.fetchone()