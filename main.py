from flask import Flask
from src.api.user.user import userBlueprint
from extensions import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
# creating application

def create_app():
    app = Flask(__name__)
    # configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pndychrg:pndychrg@localhost:5432/Trees'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']="TREEINITIATIVE"

    db.init_app(app=app)
    migrate = Migrate(app,db)
    jwt = JWTManager(app=app)
    # from src.api.user import userBlueprint
    # fetching and registering the blueprint
    app.register_blueprint(userBlueprint)
    @app.route("/")
    def index():
        return "Hello World"

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        app.run(debug=True)
