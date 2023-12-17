from main import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone}', '{self.password}')"


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    point_a = db.Column(db.String(120), nullable=False)
    point_b = db.Column(db.String(120), nullable=False)
    sch = db.relationship('Schedule', backref='driver', lazy=True)

    def __repr__(self):
        return f"(Schedule('{self.date}', '{self.point_a}', '{self.point_b}', '{self.bus}', '{self.status}')"


class Schedule(db.Model):
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), primary_key=True, nullable=False, unique=True)
    dep_t = db.Column(db.DateTime, nullable=False)
    arr_t = db.Column(db.DateTime, nullable=False)
    bus_n = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), default='unknown')

    def __repr__(self):
        return f"Schedule('{self.trip_id}', '{self.dep_t}', '{self.arr_t}', '{self.bus_n}', '{self.status}')"
