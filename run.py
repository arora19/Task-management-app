from app import create_app, db
from app.routes import initialize_routes
from flask_restful import Api

# create the flask app instance
app = create_app()

# initialize the API with Flask app
api = Api(app)
initialize_routes(api)

# create the database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
