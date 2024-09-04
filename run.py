from app import create_app, db
from sqlalchemy import inspect
# from app.routes import initialize_routes
# from flask_restful import Api

# create the flask app instance
app = create_app()
'''
# initialize the API with Flask app
api = Api(app)

initialize_routes(api)
'''
# create the database tables
with app.app_context():
    # db.drop_all()
    print("Entering app context...")
    db.create_all()
    print("Tables created")

    # Use SQLAlchemy's inspector to list tables
    # inspector = inspect(db.engine)
    # tables = inspector.get_table_names()
    # print(f"Tables in database: {tables}")

    # db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
