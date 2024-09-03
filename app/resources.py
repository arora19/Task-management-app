from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from .models import db, User, Task

# request parsers
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help='Title is required')
task_parser.add_argument('description', type=str)
task_parser.add_argument('due_date', type=str) # may need to parse this to datetime
task_parser.add_argument('priority', type=str, choices=['Low', 'Normal', 'High'], default='Normal')
task_parser.add_argument('status', type=str, choices=['Pending', 'Completed'], default='Pending')
task_parser.add_argument('user_id', type=int, required=True, help='User ID is required')


class UserResources(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return {'id': user.id, 'username': user.username}, 200