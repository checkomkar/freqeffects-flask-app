from flask import Blueprint, render_template, abort

home_page = Blueprint('home_page', __name__)

@home_page.route('/', defaults={'page': 'index'})
def home(page):
    return 'Home'