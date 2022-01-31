
from flask_mongoengine import MongoEngine


db = MongoEngine()

class graph(db.Document):
    name = db.StringField()
    title = db.StringField()
    description = db.StringField()
    graphImg = db.StringField()


class costumers(db.Document):
    costumerID = db.StringField()
    Gender = db.StringField()
    Age = db.StringField()
    Annual_income = db.StringField()
    Spending_score = db.StringField()