from flask import Flask
from flask import request
from flask import jsonify
from .corex_client import CoreXClient

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

   
    
    @app.route('/')
    def index():
        return jsonify({'hello': "world"})
    
    @app.route('/env')
    def get_environment():
        return jsonify({"ENV": app.config['ENVIRONMENT']})
    

    @app.route('/getaccountbalance')
    def get_accout_balance():

        alias = request.args.get('alias')
        corex_client = CoreXClient(app.config['COREX_BASE_URL'], 2)
        monto = corex_client.get_balance_of_account(alias)

        return {
            "status": "OK",
            "message": "El balance en su cuenta titulada %s es de %s pesos" % (alias, monto),
            "operation success": True}
    


    @app.route('/getcreditcardlimit')
    def get_credit_card_limit():

        alias = request.args.get('alias')
        corex_client = CoreXClient(app.config['COREX_BASE_URL'], 2)
        limit = corex_client.get_credit_card_limit(alias)

        return {
            "status": "OK",
            "message": "El limite de su tarjeta de crédito %s es de %s pesos" % (alias, limit),
            "operation success": True}
    

    @app.route('/getcreditcardavailablecredit')
    def get_credit_card_available_credit():

        alias = request.args.get('alias')
        corex_client = CoreXClient(app.config['COREX_BASE_URL'], 2)
        available_credit = corex_client.get_credit_card_available_credit(alias)

        return {
            "status": "OK",
            "message": "El credito disponible de su tarjeta de crédito %s es de %s pesos" % (alias, available_credit),
            "operation success": True}
    

    @app.route('/getcreditcardconsumedcredit')
    def get_credit_card_consumed_credit():

        alias = request.args.get('alias')
        corex_client = CoreXClient(app.config['COREX_BASE_URL'], 2)
        consumed_credit = corex_client.get_credit_card_consumed_credit(alias)

        return {
            "status": "OK",
            "message": "El credito consumido de su tarjeta de crédito %s es de %s pesos" % (alias, consumed_credit),
            "operation success": True}
    
    return app
