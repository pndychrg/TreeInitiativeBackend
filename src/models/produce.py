from extensions import db


class Produce(db.Model):

    __tablename__ = 'produce'
    id = db.Column(db.Integer, primary_key=True)
    tree_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    name = db.Column(db.String(), nullable=False)

    def toJson(self):
        return {
            "id": self.id,
            "tree_id": self.tree_id,
            "name": self.name
        }
