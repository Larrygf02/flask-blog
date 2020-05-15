from app import app
from models import User
from flask import jsonify, request
from utils import to_dict, exists

@app.route("/login")
def login():
    body = request.get_json()
    user = User.query.filter_by(**body)
    if exists(user):
        data = {"is_login": True, "user": **to_dict(user.first(), ['password'])}
        return jsonify({"status": True, "data": data })
    return jsonify({"status": True, "data": { "is_login": False}})