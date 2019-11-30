from flask import Flask, jsonify, request
from data import users

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(users)

@app.route('/user/<id>', methods=["GET"])
def get_user(id):
    return next(filter(lambda u: u["id"] == int(id), users), {
        "status": "FAILED",
        "message": "No user with provided id"
    })

@app.route('/user', methods=["POST"])
def new_user():
    next_id = max(map(lambda u: u["id"], users)) + 1
    user = request.json
    users.append(dict(id=next_id, first_name=user["first_name"], last_name=user["last_name"]))
    return {
        "status": "CREATED",
        "user": user
    }

@app.route('/user/<id>', methods=["PATCH", "PUT"])
def patch_user(id):
    user = next(filter(lambda u: u["id"] == int(id), users), None)
    if user:
        user.update(request.json)
        return {
            "status": "UPDATED",
            "user": user
        }
    else:
        return {
            "status": "FAILED",
            "message": "No user matches id"
        }

@app.route('/user/<id>', methods=["DELETE"])
def delete_user(id):
    idx = next((index for (index, u) in enumerate(users) if u["id"] == int(id)), None)
    if idx:
        del users[idx]
        return {
            "status": "SUCCESS",
            "users": users
        }
    else:
        return {
            "status": "FAILED",
            "message": "No users with given id"
        }
