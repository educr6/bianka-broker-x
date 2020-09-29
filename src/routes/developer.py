from flask import Blueprint, current_app
from flask import jsonify


developer = Blueprint('developer', __name__, url_prefix='/dev')

@developer.route('/env')
def get_environment():
        return jsonify({"ENV": current_app.config['ENVIRONMENT']})

@developer.route('/')
def index():
        return jsonify({'hello': "world"})




   