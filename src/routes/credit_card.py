from flask import Blueprint, current_app
from flask import jsonify
from flask import request
from flask import Response


from ..corex_clients.credit_card import CreditCardsCoreXClient
from ..phrase_builders import transactions as transactionsPhraseBuilder


credit_card = Blueprint('credit_card', __name__)



@credit_card.route('/getcreditcardlimit')
def get_credit_card_limit():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    limit = corex_client.get_credit_card_limit(alias)

    if (limit == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400


    return {
        "status": "OK",
        "message": "El limite de su tarjeta de crédito %s es de %s pesos" % (alias, limit),
        "operation success": True}

@credit_card.route('/getmissingdays')
def getmissingdays():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    missing_days = corex_client.get_missing_days(alias)

    if (missing_days == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400
    
    if (missing_days == 1):
        speak_output = "A usted le falta  solo un día para pagar su tarjeta de crédito %s" % alias
    else:
        speak_output = "A usted le faltan %s dias para pagar su tarjeta de credito %s" % (missing_days, alias)


    return {
        "status": "OK",
        "message": speak_output,
        "operation success": True}



@credit_card.route('/getcreditcardavailablecredit')
def get_credit_card_available_credit():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    available_credit = corex_client.get_credit_card_available_credit(alias)

    if (available_credit == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400


    return {
        "status": "OK",
        "message": "El credito disponible de su tarjeta de crédito %s es de %s pesos" % (alias, available_credit),
        "operation success": True}
    


@credit_card.route('/getcreditcardconsumedcredit')
def get_credit_card_consumed_credit():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    consumed_credit = corex_client.get_credit_card_consumed_credit(alias)

    if (consumed_credit == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400


    return {
        "status": "OK",
        "message": "El credito consumido de su tarjeta de crédito %s es de %s pesos" % (alias, consumed_credit),
        "operation success": True}


@credit_card.route('/getcreditcardminimumpayment')
def get_credit_card_minimum_payment():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    minimum_payment = corex_client.get_credit_card_minimum_payment(alias)

    if (minimum_payment == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "El pago mínimo de su tarjeta de crédito %s es de %s pesos" % (alias, minimum_payment),
        "operation success": True}



@credit_card.route('/getcreditcardcutpayment')
def get_credit_card_cut_payment():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    cut_payment = corex_client.get_credit_card_cut_payment(alias)


    if (cut_payment == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "El pago al corte de su tarjeta de crédito %s es de %s pesos" % (alias, cut_payment),
        "operation success": True
        }
    

@credit_card.route('/getcreditcardtransactions')
def get_credit_card_transactions():

    alias = request.args.get('alias')
    number_of_transactions = int(request.args.get('numberoftransactions'))
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    transactions = corex_client.get_credit_card_transactions(alias)

   
    
    if (transactions == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400
    
    message = transactionsPhraseBuilder.create_transactions_phrase(transactions, number_of_transactions)

    return {
        "status": "OK",
        "message": message,
        "operation success": True
        }

<<<<<<< HEAD
@credit_card.route('/getcreditcardcutday')
def get_credit_card_cut_day():
=======
@credit_card.route('/paycreditcard', methods=['POST'])
def pay_credit_card():

    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2, {"Authorization": "%s %s" % (current_app.config['AUTH_HEADER_TYPE'], current_app.config['AUTH_HEADER_VALUE'])})
    transfer_petition = request.json

    transfer_transaction = corex_client.pay_credit_card(transfer_petition)

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
    


    

>>>>>>> 1784d9aa68b7586b852b802a0ba1df7c098b0d59

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    cut_day = corex_client.get_credit_card_cut_day(alias)


    if (cut_day == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "La fecha proxima fecha de corte de su tarjeta de credito %s es el %s" % (alias, cut_day),
        "operation success": True
        }

@credit_card.route('/getcreditcardpaymentlimitdate')
def get_credit_card_payment_limit_date():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    limit_day = corex_client.get_credit_card_payment_limit_date(alias)


    if (limit_day == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "La fecha limite para el pago de la tarjeta de credito %s es el %s" % (alias, limit_day),
        "operation success": True
        }



@credit_card.route('/getcreditcarddayslefttopay')
def get_credit_card_days_left_to_pay():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    days_limit_payment = corex_client.get_credit_card_days_left_to_pay(alias)


    if (days_limit_payment == None):
        content =  {
            "status": "BAD REQUEST",
            "message": "No pudimos encontrar su tarjeta titulada %s" % alias,
            "operation success": False
        }

        return content, 400

    return {
        "status": "OK",
        "message": "Dispone de %s dias para pagar la tarjeta de credito %s" % (days_limit_payment, alias),
        "operation success": True
        }
        
    