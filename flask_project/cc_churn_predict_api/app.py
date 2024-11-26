import cc_churn

from flask import Flask, request, redirect, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import os

from custom_transformer import DropColumns

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.get_json()
            predictOutput = cc_churn.predict(data)
            return jsonify({"prediction": int(predictOutput[0])})        
        
        except Exception as error:
           # return {"error": error}
            return make_response(jsonify(error), 500)


api.add_resource(Test,'/')
api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == '__main__':
    app.run(debug=True)