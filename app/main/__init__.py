from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import datetime

from .config import config_by_name
flask_bcrypt = Bcrypt()
mdb = MongoEngine()
emailSalt = URLSafeTimedSerializer('Thisisasecret!')

def create_app(config_name):
    app = Flask(__name__,template_folder="views")
    app.config.from_object(config_by_name[config_name])

    flask_bcrypt.init_app(app)
    mdb.init_app(app)
    return app