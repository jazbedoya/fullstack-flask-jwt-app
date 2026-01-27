from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Order
from extensions import db

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders", methods=["POST"])
@jwt_required()
def create_order():
    data = request.json

    # convertir el id a INT
    user_id = int(get_jwt_identity())

    order = Order(
        user_id=user_id,
        items=data["items"],
        total=data["total"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"msg": "Order created successfully"}), 201
