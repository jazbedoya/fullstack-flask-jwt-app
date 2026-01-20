from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models import Item
from extensions import db


#este codigo detiene la ejecucion de la ruta si no eres el admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        claims = get_jwt()  
        if claims.get("role") != "admin":
            return {"msg": "Admins Only"}, 403
        return fn(*args, **kwargs)
    return wrapper
    

items_bp = Blueprint("items", __name__)

@items_bp.route("/items", methods=["GET"])
@jwt_required() #usuario debe estar autenticado
def get_items():
    items = Item.query.all() #trae todo los items
    return jsonify([
       { "id": i.id, "name" : i.name, "description": i.description} #convierte los objestos de la base de datos en json
        for i in items
    ])


#solo puede hacerlo un admin y estar autenticado
@items_bp.route("/items", methods=["POST"])
@jwt_required()
@admin_required
def create_item():
    data = request.json
    item =Item(
        name = data["name"], 
        description = data.get("description"))
    
    db.session.add(item)
    db.session.commit()
    return jsonify({"msg":"ITEM CREATED!"}),201


@items_bp.route("/items/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_item(id):
    item = Item.query.get_or_404(id) #busca el item con ese id si no existe error 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"msg": "ITEM DELETED"})

