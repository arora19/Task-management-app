from flask_restful import Api, Resource
from .resources import UserResource, TaskResource


def initialize_routes(api: Api):
    print("Initializing routes...")
    # Add print statements to see which routes are registered
    print(f"Existing endpoints before: {api.resources}")
    # route for managing a single user
    api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user')

    # Route for managing all users (create new users)
    api.add_resource(UserResource, '/users', endpoint='users')

    # route for managing a single task
    api.add_resource(TaskResource, '/tasks/<int:task_id>', endpoint='task')

    # route for managing all tasks (create new tasks)
    api.add_resource(TaskResource, '/tasks', endpoint='tasks')

    print("Routes initialized.")
    print(f"Existing endpoints after: {api.resources}")

    class TestResource(Resource):
        def get(self):
            return {'message': 'API is working'}, 200

    # Add this line to initialize routes
    api.add_resource(TestResource, '/test')