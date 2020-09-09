
from flask import Flask
from flask import request
from flask import jsonify
from .corex_client import CoreXClient
from . import routes

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    routes.register_routes(app)
    

    return app