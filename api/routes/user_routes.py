from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from api.controllers.user_controller import UserController
from api.middlewares.auth import token_required

user_controller = UserController()


@app.route('/api/user/<int:id>')
@cross_origin()
@token_required
def get_user_by_id(id):
    return jsonify(user_controller.get_user_by_id(id))


@app.route('/api/users')
@cross_origin()
@token_required
def get_users():
    return jsonify(user_controller.get_all_users())


@app.route('/api/user', methods=['POST'])
@cross_origin()
@token_required
def add_user():
    return jsonify(user_controller.add_user(request))


@app.route('/api/user/<int:id>', methods=['DELETE'])
@cross_origin()
@token_required
def delete_user(id):
    return jsonify(user_controller.delete_user(id))
