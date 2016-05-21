import os
from flask import Flask, jsonify
from flask.ext import restful
from collections import OrderedDict
import simplejson


app = Flask(__name__)
api = restful.Api(app)

class GetResume(restful.Resource):
    def get(self):
        #Read in JSON resume
        with open('matt_resume.json', 'r') as f:
            resume = simplejson.load(f, object_pairs_hook=OrderedDict)

        return jsonify(resume)


api.add_resource(GetResume, '/api/1.0/getresume', endpoint = 'getresume')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)