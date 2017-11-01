from flask import Blueprint, request
from bson import Binary, Code
from bson.json_util import dumps
from . import mongo


products_page = Blueprint('products_page', __name__)



@products_page.route('/products', methods=['POST','GET'])
def products():
    if request.method == 'GET':
        products = mongo.db.products.find({})
        print (products)
        return dumps(products)