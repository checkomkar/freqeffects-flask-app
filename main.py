from flask import Flask, Blueprint, render_template, url_for, request, session, jsonify, redirect
from flask.ext.pymongo import PyMongo
from bson import Binary, Code
from bson.json_util import dumps
import bcrypt
from routes.home import home_page
from routes.products import products_page
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'freqeffects'
app.config['MONGO_URI'] = 'mongodb://freqeffects:digjam@ds243055.mlab.com:43055/freqeffects'

mongo = PyMongo(app)

def register_blueprints(app):
    app.register_blueprint(home_page)
    app.register_blueprint(products_page)
# @app.route('/')
# def index():
#     return 'Home'

# @app.route('/products', methods=['POST','GET'])
# def products():
#     if request.method == 'GET':
#         products = mongo.db.products.find({})
#         print (products)
#         return dumps(products)
    

    



if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)