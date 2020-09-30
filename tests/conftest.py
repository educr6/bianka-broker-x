from flask import Flask, jsonify


import pytest
import sys
import os

sys.path.append(os.path.abspath('../src'))

from src import create_app as flask_app
from src.corex_clients.credit_card import CreditCardsCoreXClient
from src.corex_clients.account import AccountsCoreXClient
from src.corex_clients.base import CoreXClient


@pytest.fixture
def app():
    yield flask_app()


@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def base_corex_client(app):
    return CoreXClient(app.config['COREX_BASE_URL'], 2)

@pytest.fixture
def account_corex_client(app):
    return AccountsCoreXClient(app.config['COREX_BASE_URL'], 2)

@pytest.fixture
def credit_card_corex_client(app):
    return CreditCardsCoreXClient(app.config['COREX_BASE_URL'], 2)
