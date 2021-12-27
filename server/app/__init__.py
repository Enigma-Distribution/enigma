
import os
from flask import Flask
# from config import Config

# template_dir1 = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir1 = os.path.join(template_dir1, 'enigma-frontEnd')

# template_dir = os.path.join(template_dir1, 'templates')
# hard coded absolute path for testing purposes

# template_dir = os.path.abspath('../../enigma-frontEnd')
app = Flask(__name__)  # , template_folder=template_dir
# app.static_folder = os.path.join(template_dir1, 'static')
# app.config.from_object(Config)
from app import services