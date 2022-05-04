# from app import app
from app.properties import get_site_secret_key
import os
from flask import Flask
from flask_cors import CORS
from flask_apscheduler import APScheduler
from app.datastore import steps as steps_db
import datetime

app = Flask(__name__)  # , template_folder=template_dir
app.config['SECRET_KEY'] = get_site_secret_key()

CORS(app)

# from app import services

from app.services.auth_service import app as auth_service
app.register_blueprint(auth_service)

from app.services.task_service import app as task_service
app.register_blueprint(task_service)

from app.services.step_service import app as step_service
app.register_blueprint(step_service)

from app.services.worker_service import app as worker_service
app.register_blueprint(worker_service)
 
from app.uploads.routes import uploads
app.register_blueprint(uploads)

#function executed by scheduled job
# https://stackoverflow.com/questions/55427781/is-there-a-way-to-run-python-flask-function-every-specific-interval-of-time-and
def my_job(text):
    print(text, str(datetime.datetime.now()))
    # Find all the steps that 
    # 1) have been asigned to someone AND
    # 2) It has been more than 4 mins since they were assigned AND
    # 3) They have not been finished

    # Set their alloted_to field to None and add these to queues.

    steps_db.update_already_assigned_delayed_incomplete_steps()


if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.add_job(func=my_job, args=['job run'], trigger='interval', id='job', seconds=5)
    scheduler.start()
    app.run()