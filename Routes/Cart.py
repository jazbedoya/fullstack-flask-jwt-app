from flask import Blueprint, request, jsonify #Blueprint permite dividir la app Flask en módulos ,rutas separadas
from flask_jwt_extended import jwt_required, get_jwt_identity

cart_bp = Blueprint("cart", __name__)

cart_storage = {}  #carrito en memoria Es un diccionario en memoria

@cart_bp.route("/cart", methods=["POST"])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    item = request.json #lee el body

    cart_storage.setdefault(user_id, []) #Si el usuario no tiene carrito, crea uno vacío
    cart_storage[user_id].append(item) #añade product a cart

    return jsonify(cart_storage[user_id])


@cart_bp.route("/cart", methods=["GET"])
@jwt_required()
def get_cart():
    user_id = get_jwt_identity() #identifica usuario logueado
    return jsonify(cart_storage.get(user_id, [])) #si el usu tiene carrito lo devuelve si no []



#cada usuario tiene su propio carrito 
