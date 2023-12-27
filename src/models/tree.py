from extensions import db


class Tree(db.Model):

    __tablename__ = 'tree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    species = db.Column(db.String(), nullable=False)
    height_meters = db.Column(db.Integer, nullable=False)
    age_years = db.Column(db.Integer, nullable=False)
    available_trees = db.Column(db.Integer, nullable=False)
    total_trees = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String())

    # produce
    produces = db.relationship("Produce", backref="Tree")

    def toJson(self):
        return {"id": 1,
                "name": "Oak",
                "species": "Quercus",
                "height_meters": 25,
                "age_years": 80,
                "produce": [
                    "wood",
                    "acorns"
                ],
                "available_trees": 3,
                "total_trees": 10,
                "notes": "Tall and sturdy deciduous tree with distinctive lobed leaves."
                }
