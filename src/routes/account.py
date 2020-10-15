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
            "operation_success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "El balance en su cuenta titulada %s es de %s pesos" % (alias, monto),
        "operation_success": True}

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
            "operation_success": False
        }

        return content, 400
    
    message = transactionsPhraseBuilder.create_transactions_phrase(transactions, number_of_transactions)

    return {
        "status": "OK",
        "message": message,
        "operation_success": True
        }
    
@account.route('/transfermoneytobeneficiary', methods=['POST'])
def transfer_money_to_beneficiary():

    corex_client = AccountsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    transfer_petition = request.json

    transfer_transaction = corex_client.transfer_money_to_beneficiary(transfer_petition)

    if (transfer_transaction["success"] != True):
        content =  {
            
            "message": transfer_transaction["message"],
            "operation_success": False
        }

        return content, 400
    
    key_number = transfer_transaction["keyNumber"]


    
    return {
        "status": "OK",
        "message": "Favor indique su clave #%s" % key_number,
        "keyNumber": key_number,
        "current_operation_id": transfer_transaction["rowUiDTransaction"],
        "operation_success": True
        }

@account.route('/completetransfertobeneficiary', methods=['POST'])
def complete_transfer_to_beneficiary():

    corex_client = AccountsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    complete_transfer_petition = request.json

    complete_transfer_petition = corex_client.complete_transfer_to_beneficiary(complete_transfer_petition)

    if (complete_transfer_petition["success"] != True):
        
        content =  {
            "message": complete_transfer_petition["message"],
            "operation_success": False
        }

        return content, 400
    
   
    return {
        "message": "Su transferencia ha sido completada.",
        "operation_success": True
        }