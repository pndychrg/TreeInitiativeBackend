from extensions import db
from src.models.user import User
from sqlalchemy import exc

class UserDB:

    def checkIfUserExists(self,username):
        user = User.query.filter(User.username==username).first()
        return user

    def createUser(self,name,username,password):
        # checking if a user with same username exists or not
        existingUser = self.checkIfUserExists(username=username)
        if existingUser:
            return "User already exists with same username",False
        try:
            
            new_user = User(name=name,username=username,password=password)
            db.session.add(new_user)
            db.session.commit()
            return new_user,True
        except exc.IntegrityError:
            return "Error occured",False

    def loginUser(self,username,password):
        
        existingUser = self.checkIfUserExists(username=username)
        if existingUser:
            # checking for password
            if existingUser.password == password:
                return existingUser,True
            else:
                return "Incorrect password",False
        else:
            return "invalid username",False