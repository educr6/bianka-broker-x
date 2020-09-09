from .account import account
from .credit_card import credit_card
from .developer import developer
from .home import home

def register_routes(app):
    app.register_blueprint(account)
    app.register_blueprint(credit_card)
    app.register_blueprint(developer)
    app.register_blueprint(home)
