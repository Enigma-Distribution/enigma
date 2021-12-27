from app.datastore import tasks as tasks_db
from uuid import uuid4
from time import time
from app.exceptions import TaskNotFoundException

def create_task(user, name, mapfile_id, reducefile_id, data_source, status):
    task = {
        "task_id": str(uuid4()),
        "user": user,
        "name": name,
        "date_created": str(int(time())),
        "mapfile_id": mapfile_id,
        "reducefile_id": reducefile_id,
        "data_source": data_source,
        "status": status
    }
    tasks_db.insert_task(task, user)
    return task

def get_all_tasks(user):
    taskdata = tasks_db.select_all_tasks(user)
    data = []
    for task in taskdata:
        data.append({
            "task_id": task[0],
            "name":  task[1],
            "date_created": task[2],
            "mapfile_id":  task[3],
            "reducefile_id":  task[4],
            "data_source":  task[5],
            "status": task[6],
            })
    return data

def get_selected_task(task_id, user):
    task_details = tasks_db.select_specific_task(task_id, user)
    if not task_details:
        raise TaskNotFoundException
    task = {
            "task_id": task[0],
            "name":  task[1],
            "date_created": task[2],
            "mapfile_id":  task[3],
            "reducefile_id":  task[4],
            "data_source":  task[5],
            "status": task[6],
        }
    return task