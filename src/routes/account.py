from flask import Blueprint, current_app
from flask import jsonify
from flask import request

from ..phrase_builders import transactions as transactionsPhraseBuilder
from ..corex_clients.account import AccountsCoreXClient


account = Blueprint('account', __name__)


@account.route('/getaccountbalance')
def get_accout_balance():

    alias = request.args.get('alias')
    corex_client = AccountsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    monto = corex_client.get_balance_of_account(alias)

    if (monto == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "Usted no posee una cuenta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "El balance en su cuenta titulada %s es de %s pesos" % (alias, monto),
        "operation success": True}

@account.route('/getaccounttransactions')
def get_account_transactions():

    alias = request.args.get('alias')
    number_of_transactions = int(request.args.get('numberoftransactions'))
    corex_client = AccountsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    transactions = corex_client.get_account_transactions(alias)

   
    
    if (transactions == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su cuenta titulada %s" % alias,
            "operation success": False
        }

        return content, 400
    
    message = transactionsPhraseBuilder.create_transactions_phrase(transactions, number_of_transactions)

    return {
        "status": "OK",
        "message": message,
        "operation success": True
        }