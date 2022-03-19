from app.datastore import steps as steps_db
from app.interfaces import tasks as task_service
from uuid import uuid4
from time import time
from app.exceptions import TaskNotFoundException

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
    step = {
        "phase": phase,
        "datasource_id": datasource_id,
        "step_id": step_id
    }
    steps_db.update_completed_step(step)
    return step

def update_completed_reduce_step():
    step = {
        "is_completed": 1,
        "step_id": step_id
    }
    steps_db.update_completed_reduce_step(step)
    return

def is_task_completed():
    task_id = steps_db.get_task_id(step_id)
    steps_unfinished_in_reduce_phase = steps_db.get_steps_unfinished_in_reduce_phase(task_id)
    if count(steps_unfinished_in_reduce_phase)>0:
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
            "assigned_to": step[4],
            "is_completed": step[5],
            "result_file_id": step[6],
            "step_size": step[7],
        })
    return data

def get_step_to_allot(step_phase):
    step = steps_db.get_step_to_allot(step_phase)
    return step
