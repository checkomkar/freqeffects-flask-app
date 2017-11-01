rom flask import Flask, Blueprint, render_template, url_for, request, session, jsonify, redirect
from flask.ext.pymongo import PyMongo

import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'freqeffects'
app.config['MONGO_URI'] = 'mongodb://freqeffects:digjam@ds243055.mlab.com:43055/freqeffects'

mongo = PyMongo(app)