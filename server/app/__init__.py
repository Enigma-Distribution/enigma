from app.properties import get_site_secret_key
import os
from flask import Flask
from flask_cors import CORS
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