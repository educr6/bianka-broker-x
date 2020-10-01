from flask import Blueprint, current_app
from flask import jsonify
from flask import request
from flask import Response

from ..corex_clients.credit_card import CreditCardsCoreXClient


credit_card = Blueprint('credit_card', __name__)



@credit_card.route('/getcreditcardlimit')
def get_credit_card_limit():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
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

    

@credit_card.route('/getcreditcardavailablecredit')
def get_credit_card_available_credit():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
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
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
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
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
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
        "message": "No pudimos encontrar su tarjeta de crédito %s es de %s pesos" % (alias, minimum_payment),
        "operation success": True}



@credit_card.route('/getcreditcardcutpayment')
def get_credit_card_cut_payment():

    alias = request.args.get('alias')
    corex_client = CreditCardsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
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


        
    