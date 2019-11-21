import models
from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash,check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

#creating blueprint
user = Blueprint('users','user')

#user create route
@user.route('/register', methods=["POST"])
def register():
    payload = request.get_json()
    payload['email']= payload['email']
    #see if user already exists
    try:
        models.User.get(models.User.email==payload['email'])
        return jsonify(data={}, status={'code':401, 'message': 'email has already been registered'})
    except models.DoesNotExist:
        payload['password']= generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        login_user(user)
        user_dict = model_to_dict(user)
        #remove password from response object
        del user_dict['password']
        return jsonify(data=user_dict, status={'code': 201, 'message': 'Success'})
        
@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    try:
        user = models.User.get(models.User.email==payload['email'])
        user_dict = model_to_dict(user)
        if check_password_hash(user_dict['password'], payload['password']):
            del user_dict['password']
            login_user(user)
            return jsonify(data=user_dict, status={'code': 201,'message':'success'})
        else:
            return jsonify(data= {}, status={'code':401,'message':'Username or Password Incorrect'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code':401,'message':'Username or Password Incorrect'})
@user.route("/<id>", methods=["GET"])
def get_User(id):
    print(id)
    user = models.User.get_by_id(id)
    return jsonify(data=model_to_dict(user), status={"code":200, "message": "Success"})


