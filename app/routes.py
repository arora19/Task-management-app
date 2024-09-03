from flask_restful import Api
from .resources import UserResource, TaskResource


def initialize_routes(api: Api):
    # route for managing a single user
    api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user')

    # route for managing a single task
    api.add_resource(TaskResource, '/tasks/<int:task_id>', endpoint='task')

    # route for managing all tasks (create new tasks)
    api.add_resource(TaskResource, '/tasks', endpoint='tasks')
