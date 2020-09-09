from flask import Blueprint, current_app
from flask import jsonify
from flask import request
from ..corex_clients.account import AccountsCoreXClient


account = Blueprint('account', __name__)


@account.route('/getaccountbalance')
def get_accout_balance():

    alias = request.args.get('alias')
    corex_client = AccountsCoreXClient(current_app.config['COREX_BASE_URL'], 2)
    monto = corex_client.get_balance_of_account(alias)

    return {
        "status": "OK",
        "message": "El balance en su cuenta titulada %s es de %s pesos" % (alias, monto),
        "operation success": True}