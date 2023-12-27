from extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable=False)
    username = db.Column(db.String(),nullable=False,unique=True)
    password = db.Column(db.String(),nullable=False)

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}"
    
    def toJson(self):
        return {
            "id":self.id,
            "name":self.name,
            "username":self.username,
        }