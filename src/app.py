from flask import Flask
from flask import request
from .brokerx_client import get_balance_of_account

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

   
    
    @app.route('/')
    def index():
        return "Hello World"
    

    @app.route('/getaccountbalance')
    def get_accout_balance():

        alias = request.args.get('alias')
        monto = get_balance_of_account(2, alias)

        return {
            "status": "OK",
            "message": "El balance en su cuenta titulada %s es de %s pesos" % (alias, monto),
            "operation success": True}
    
    return app

