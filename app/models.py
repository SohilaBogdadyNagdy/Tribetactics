from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType
from . import db

class User(UserMixin, db.Model):
    TYPES = [
        (u'ADMIN', u'admin'),
        (u'USER', u'user'),
        (u'RESTAURANT', u'restaurant')
    ]
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    type = db.Column(ChoiceType(TYPES))

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    owner=db.Column(db.Integer, db.ForeignKey('user.id'))
    #menu = db.Column(db.ARRAY(db.JSON))

class Order(db.Model):
    STATES = [
        (u'PENDING', u'Pending'),
        (u'DELIVERED', u'Delivered'),
    ]
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(ChoiceType(STATES))
    user=db.Column(db.Integer, db.ForeignKey('user.id'))
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    #items = db.Column(db.ARRAY(db.JSON),server_default="{}")
    totalAmount = db.Column(db.Integer)
