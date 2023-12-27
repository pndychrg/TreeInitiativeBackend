from flask import Blueprint, request
from flask_restful import reqparse
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.backend.user import UserDB

# init backend
userDB = UserDB()
userBlueprint = Blueprint('user', __name__)
# route for user login


@userBlueprint.route('/login', methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if (username == None or password == None):
        return "Insufficient Data"

    response, status = userDB.loginUser(username=username, password=password)
    if status:
        token = create_access_token(
            identity=response.toJson(), expires_delta=timedelta(hours=24))
        return token, 200
    # return f"{response},{status}"
    else:
        return f"{response}", 400


create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("name",type=str,help="This field cannot be blank",required=True)
create_user_parser.add_argument("username",type=str,help="This field cannot be blank",required=True)
create_user_parser.add_argument("password",type=str,help="This field cannot be blank",required=True)


# route for user signup
@userBlueprint.route('/register', methods=['GET', 'POST'])
def register():
    data = create_user_parser.parse_args()
    # add validators here
    response,status = userDB.createUser(
        name=data['name'],username=data['username'],password=data['password']
    )
    if status:
        token = create_access_token(
            identity=response.toJson(), expires_delta=timedelta(hours=24))
        return token,200
    else:
        return {'msg':response},400
    # return "Register"
