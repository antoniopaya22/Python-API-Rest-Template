from flask_cors import cross_origin
from flask import request, jsonify
from src import app
from src.middlewares.auth import Auth

auth = Auth()

@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    return jsonify(auth.login(request))