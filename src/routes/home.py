from flask import Blueprint, current_app
from flask import jsonify


home = Blueprint('home', __name__)



@home.route('/')
def index():
        return jsonify({'hello': "world"})