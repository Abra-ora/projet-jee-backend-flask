from mongoengine import connect, Document, fields


connect('kmeans', host='127.0.0.1', port=27017)

class graph(Document):
    name = fields.StringField()
    title = fields.StringField()
    description = fields.StringField()
    graphImg = fields.StringField()


graph(name="graph test", description="description", graphImg="image").save()
