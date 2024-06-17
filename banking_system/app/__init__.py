from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
# from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.Config')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

from app import views, models
