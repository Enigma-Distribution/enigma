from app.properties import get_pg_connection

QUERY_INSERT_TASK = "INSERT INTO task(task_id, user_id, task_name, task_description, task_zip_file_id, datasource_size, task_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"

QUERY_GET_ALL_TASKS = "SELECT task_id, task_name, task_description, task_created_ts, task_zip_file_id, datasource_size, task_status FROM task WHERE user_id = %s ORDER BY task_created_ts DESC"

QUERY_GET_SPECIFIC_TASK = "SELECT task_id, task_name, task_description, task_created_ts, task_zip_file_id, datasource_size, task_status, result_file_id FROM task WHERE task_id = %s AND user_id = %s"

QUERY_UPDATE_COMPLETE_TASK = "UPDATE task SET task_status = %s, result_file_id=%s  WHERE task_id = %s"

QUERY_GET_ZIP_FILE_ID_FROM_TASK_ID = "SELECT task_zip_file_id FROM task WHERE task_id = %s"

db = get_pg_connection()

def insert_task(task, user):
    values = (task['task_id'], user, task['task_name'], task['task_description'], task['task_zip_file_id'], task['datasource_size'], task['task_status'])
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
            
def update_completed_task(task_id, result_file_id):
    values = (True, result_file_id, task_id)
    print('Before update_completed_task', values)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_UPDATE_COMPLETE_TASK, values)
            # return cursor.fetchone()

def get_zip_file_id(task_id):
    values = (task_id,)
    with db:
        with db.cursor() as cursor:
            cursor.execute(QUERY_GET_ZIP_FILE_ID_FROM_TASK_ID, values)
            return cursor.fetchone()