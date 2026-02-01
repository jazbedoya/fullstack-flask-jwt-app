from flask import Blueprint, jsonify, request
import requests
from flask_jwt_extended import jwt_required

external_bp = Blueprint("external", __name__)

# ---------- FUNCIÓN AUXILIAR ----------
# Se encarga de traer y normalizar los productos de la API externa
def fetch_external_products():
    categories = [
        "mens-shirts",
        "womens-dresses"
    ]

    products = []

    for category in categories:
        res = requests.get(
            f"https://dummyjson.com/products/category/{category}",
            timeout=10
        )

        if res.status_code == 200:
            data = res.json()
            for p in data.get("products", []):
                products.append({
                    "id": p["id"],
                    "name": p["title"],
                    "brand": p.get("brand", ""),
                    "price": p["price"],
                    "image": p["thumbnail"],
                    "category": category
                })

    return products


# ---------- RUTA PRINCIPAL ----------
@external_bp.route("/external", methods=["GET"])
@jwt_required()
def get_external_products():
    products = fetch_external_products()
    return jsonify(products)


# ---------- RUTA DE PRODUCTOS RELACIONADOS ----------
@external_bp.route("/external/related", methods=["GET"])
@jwt_required()
def external_related():
    category = request.args.get("category")

    if not category:
        return {"msg": "Category query param is required"}, 400

    products = fetch_external_products()

    related = [
        p for p in products if p["category"] == category
    ][:4]

    return jsonify(related)