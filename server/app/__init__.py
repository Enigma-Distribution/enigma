
import os
from flask import Flask
app = Flask(__name__)  # , template_folder=template_dir

from app import services

from app.uploads.routes import uploads
app.register_blueprint(uploads)