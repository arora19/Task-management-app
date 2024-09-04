from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id - unique identifier for each user
    username = db.Column(db.String(80), unique=True, nullable=False)  # username- for the user must be unique
    password = db.Column(db.String(120), nullable=False)  # user's password
    tasks = db.relationship('Task', backref='user', lazy=True)
    # tasks- relationship indicating that a user can have multiple tasks


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # title of task- required
    description = db.Column(db.String(500))  # optional description for task
    # due_date = db.Column(db.DateTime, default=datetime.utcnow)  # due date of task, default value of current time
    # priority = db.Column(db.String(50), default='Normal')  # priority level(e.g low, normal, high) with default value
    status = db.Column(db.String(50), default='Pending')  # status- (pending, completed) with default value
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # foreign key linking task to user
