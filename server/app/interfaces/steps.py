from app.datastore import steps as steps_db
from app.interfaces import tasks as task_service
from uuid import uuid4
from time import time
from app.exceptions import TaskNotFoundException
from datetime import datetime    
import pytz

def create_step(task_id, datasource_id, phase, assigned_to, is_completed, result_file_id, step_size):
    step = {
        "step_id": str(uuid4()),
        "task_id": task_id,
        "datasource_id": datasource_id,
        "phase": phase,
        "assigned_to": assigned_to,
        "is_completed": is_completed,
        "result_file_id": result_file_id,
        "step_size": step_size,
    }
    steps_db.insert_step(step)
    return step

def update_completed_step(phase, datasource_id, step_id):
    tz_NY = pytz.timezone('Asia/Kolkata')   
    datetime_NY = datetime.now(tz_NY)
    step = {
        "phase": phase,
        "datasource_id": datasource_id,
        "step_id": step_id,
        "step_updated_ts": datetime_NY
    }
    step = steps_db.update_completed_step(step)
    task_id = steps_db.get_task_id(step_id)
    return task_id

def update_completed_reduce_step(step_id):
    tz_NY = pytz.timezone('Asia/Kolkata')   
    datetime_NY = datetime.now(tz_NY)
    step = {
        "is_completed": 1,
        "step_id": step_id,
        "step_updated_ts": datetime_NY
    }
    step = steps_db.update_completed_reduce_step(step)
    task_id = steps_db.get_task_id(step_id)
    return task_id

def is_task_completed(step_id):
    print("Is task completed called with step_id", step_id)
    task_id = steps_db.get_task_id(step_id)
    steps_unfinished_in_reduce_phase = steps_db.get_steps_unfinished_in_reduce_phase(task_id)
    if len(steps_unfinished_in_reduce_phase)>0:
        return False
    else:
        task_service.update_completed_task(task_id)
        return True

def get_all_steps(task_id):
    stepdata = steps_db.select_all_steps_for_task_id(task_id)
    data = []
    for step in stepdata:
        print(step)
        data.append({
            "step_id": step[0],
            "task_id": step[1],
            "datasource_id": step[2],
            "phase": step[3],
            "step_created_ts": step[4],
            "step_updated_ts": step[5],
            "assigned_to": step[6],
            "is_completed": step[7],
            "result_file_id": step[8],
            "step_size": step[9],
        })
    return data

def get_step_to_allot(step_phase):
    step = steps_db.get_step_to_allot(step_phase)
    task_id = step[1]
    zip_file_id = task_service.get_zip_file_id(task_id)
    step_data = []
    step_data.append({
        "step_id": step[0],
        "task_id": step[1],
        "datasource_id": step[2],
        "phase": step[3],
        "zip_file_id": zip_file_id[0]
    })
    return step_data

def get_task_of_specific_step(step_id):
    step = steps_db.get_step_to_allot(step_phase)
    task_id = step[1]
    zip_file_id = task_service.get_zip_file_id(task_id)
    step_data = []
    step_data.append({
        "step_id": step[0],
        "task_id": step[1],
        "datasource_id": step[2],
        "phase": step[3],
        "zip_file_id": zip_file_id[0]
    })
    return step_data

def assign_step_to_worker(user, step_id):
    tz_NY = pytz.timezone('Asia/Kolkata')   
    datetime_NY = datetime.now(tz_NY)
    step_start_ts = datetime_NY
    steps_db.assign_step_to_worker_db(user, step_id, step_start_ts)
    return 
