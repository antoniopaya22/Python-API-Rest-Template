from flask_cors import cross_origin
from flask import request, jsonify
from api import app
from api.middlewares.auth import Auth

auth = Auth()

@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    return auth.login(request)
