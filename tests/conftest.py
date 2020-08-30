from flask import Flask, jsonify


import pytest
import sys
import os

sys.path.append(os.path.abspath('../src'))

from src import create_app as flask_app
from src.corex_client import CoreXClient


@pytest.fixture
def app():
    yield flask_app()


@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def corex_client(app):
    return CoreXClient(app.config['COREX_BASE_URL'], 2)