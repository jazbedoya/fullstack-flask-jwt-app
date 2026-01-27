from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

cors = CORS(
    resources={r"/api/*": {"origins": "*"}},
    supports_credentials=True
)
