from extensions import db


class Produce(db.Model):

    __tablename__ = 'produce'
    id = db.Column(db.Integer,primary_key=True)
    tree_id = db.Column()