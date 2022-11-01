from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Boolean, Integer
from flask_login import UserMixin

from config import *


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    

    

