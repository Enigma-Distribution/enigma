from app.datastore import tasks as tasks_db
from uuid import uuid4
from time import time
from app.exceptions import TaskNotFoundException

def create_task(user, task_name, task_description, task_zip_file_id, datasource_size, task_status):
    task = {
        "task_id": str(uuid4()),
        "user_id": user,
        "task_name": task_name,
        "task_description": task_description,
        # "task_created_ts": str(int(time())),
        "task_zip_file_id": task_zip_file_id,
        "datasource_size": datasource_size,
        "task_status": task_status,
    }
    tasks_db.insert_task(task, user)
    return task

def get_all_tasks(user):
    taskdata = tasks_db.select_all_tasks(user)
    data = []
    for task in taskdata:
        data.append({
            "task_id": task[0],
            "task_name": task[1],
            "task_description": task[2],
            "task_created_ts": task[3],
            "task_zip_file_id": task[4],
            "datasource_size": task[5],
            "task_status": task[6],
            })
    return data

def get_selected_task(task_id, user):
    task_details = tasks_db.select_specific_task(task_id, user)
    if not task_details:
        raise TaskNotFoundException
    task = {
            "task_id": task_details[0],
            "task_name": task_details[1],
            "task_description": task_details[2],
            "task_created_ts": task_details[3],
            "task_zip_file_id": task_details[4],
            "datasource_size": task_details[5],
            "task_status": task_details[6],
        }
        #add task completion status in %
    return task

def update_completed_task(task_id):
    tasks_db.update_completed_task(True, task_id)
    return task

def get_zip_file_id(task_id):
    zip_file_id = tasks_db.get_zip_file_id(task_id)
    return zip_file_id