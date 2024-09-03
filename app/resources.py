from flask_restful import Resource, reqparse
# from flask_jwt_extended import jwt_required
from .models import db, User, Task

# request parsers
# user_parser: defines the required fields for user-related queries
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

# task_parser: defines the required and optional fields for task-related requests
task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help='Title is required')
task_parser.add_argument('description', type=str)
task_parser.add_argument('due_date', type=str)  # may need to parse this to datetime
task_parser.add_argument('priority', type=str, choices=['Low', 'Normal', 'High'], default='Normal')
task_parser.add_argument('status', type=str, choices=['Pending', 'Completed'], default='Pending')
task_parser.add_argument('user_id', type=int, required=True, help='User ID is required')


class UserResource(Resource):
    # handles GET requests to retrieve a user by their ID
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404  # error
        return {'id': user.id, 'username': user.username}, 200

    # Handles POST requests to create a new user
    def post(self):
        args = user_parser.parse_args()
        if User.query.filter_by(username=args['username']).first():
            return {'message': 'Username already exists'}, 400
        new_user = User(username=args['username'], password=args['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username}, 201


class TaskResource(Resource):
    # handles GET requests to retrieve a task by its ID
    def get(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404
        return {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date.isoformat(),
            'priority': task.priority,
            'status': task.status,
            'user_id': task.user_id
        }, 200

    # Handles POST requests to create a new task
    def post(self):
        args = task_parser.parse_args()
        due_date = datetime.fromisoformat(args['due_date']) if args['due_date'] else None
        new_task = Task(
            title=args['title'],
            description=args['description'],
            due_date=args['due_date'],  # might need to parse to datetime object
            priority=args['priority'],
            status=args['status'],
            user_id=args['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return {'id': new_task.id, 'title': new_task.title}, 201
