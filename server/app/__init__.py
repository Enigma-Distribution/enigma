
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)  # , template_folder=template_dir

CORS(app)

# from app import services

from app.services.auth_service import app as auth_service
app.register_blueprint(auth_service)

from app.services.task_service import app as task_service
app.register_blueprint(task_service)

from app.uploads.routes import uploads
app.register_blueprint(uploads)