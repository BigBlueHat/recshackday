'''
Created on Apr 14, 2013

@author: byoung
'''

import requests
from flask import Flask, jsonify
from flask.ext.classy import FlaskView

app = Flask(__name__)
app.debug = True
app.testing = True

ACCESS_TOKEN = '7777b492e3beeb93b99d1f33ccbfb2b5'


class Data_SetsView(FlaskView):
    def index(self):
        return "here be data sets"


class DataView(FlaskView):
    def index(self):
        return "here be data"


class RecommendersView(FlaskView):
    def index(self):
        r = requests.get('https://api.relify.com/1/recommenders?access_token='
                         + ACCESS_TOKEN)
        rv = {'collection':
              {'version': '1', 'href': '/', 'items': []}}
        for recommender in r.json():
            links = [{'rel': 'data_set',
                      'href': '/data_sets/' + recommender['data_set_id']}]
            item = {'name': 'recommender', 'data': recommender,
                    'href': '/recommenders/' + recommender['recommender_id'],
                    'links': links}
            rv['collection']['items'].append(item)

        return jsonify(rv)

Data_SetsView.register(app)
DataView.register(app)
RecommendersView.register(app)

if __name__ == '__main__':
    app.run()
