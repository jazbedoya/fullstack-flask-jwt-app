from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/customers", methods=["GET"])
@jwt_required()
def get_customers():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"msg": "Admins only"}), 403

    users = User.query.all()
    result = []

    for user in users:
        result.append({
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "orders": [
                {
                    "id": o.id,
                    "total": o.total,
                    "created_at": o.created_at.isoformat()
                }
                for o in user.orders
            ]
        })

    return jsonify(result)

