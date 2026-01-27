from flask import Blueprint, jsonify
import requests
from flask_jwt_extended import jwt_required


external_bp=Blueprint("external", __name__)

@external_bp.route("/external", methods=["GET"])
@jwt_required()
def get_external_products():
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

    return jsonify(products)
