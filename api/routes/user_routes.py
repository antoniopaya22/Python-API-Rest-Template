from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from api.controllers.user_controller import UserController
from api.middlewares.auth import Auth

user_controller = UserController()
auth = Auth()

@app.route('/api/user/<int:id>')
@cross_origin()
def get_user_by_id(id):
    return auth.login_required(request, jsonify(user_controller.get_user_by_id(id)))

@app.route('/api/users')
@cross_origin()
def get_users():
    return  auth.login_required(request, jsonify(user_controller.get_all_users()))

@app.route('/api/user', methods=['POST'])
@cross_origin()
def add_user():
    return auth.login_required(request, jsonify(user_controller.add_user(request)))

@app.route('/api/user/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_user(id):
    return auth.login_required(request, jsonify(user_controller.delete_user(id)))
