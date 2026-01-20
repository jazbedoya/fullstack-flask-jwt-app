from flask import Flask
from config import Config
from extensions import db, jwt, cors
from Routes.auth import auth_bp
from Routes.items import items_bp
#from Routes.external_api import external_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(items_bp, url_prefix="/api")
    #app.register_blueprint(external_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
