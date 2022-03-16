from app.datastore import steps as steps_db
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