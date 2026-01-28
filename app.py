from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt

from Routes.auth import auth_bp
from Routes.items import items_bp
from Routes.external_api import external_bp
from Routes.customers import users_bp
from Routes.orders import orders_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(items_bp, url_prefix="/api")
    app.register_blueprint(external_bp, url_prefix="/api")
    app.register_blueprint(users_bp, url_prefix="/api")
    app.register_blueprint(orders_bp, url_prefix="/api")

    @app.route("/")
    def health():
        return {"status": "ok"}, 200

    return app


app = create_app()
