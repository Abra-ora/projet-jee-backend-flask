from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from module import costumers, graph, db

app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'kmeans',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)
# api = Api(app)


@app.route('/costumers')
def getCostumers():
    # graph(name="graph test", desc="description", graphImg="image").save()
    costumerss = costumers.objects
    return jsonify(costumerss)


@app.route('/graphs')
def getGraphs():
    graphs = graph.objects
    return jsonify(graphs)


if __name__ == "__main__":
    app.run(debug=True)
