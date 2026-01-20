from flask import Blueprint, request, jsonify
from models import User
from extensions import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(email=data["email"], role=data.get("role", "user"))
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "Bad credentials"}), 401

    token = create_access_token(
        identity=str(user.id),  #string      
        additional_claims={
            "role": user.role         
        }
    )

    return jsonify(token=token), 200