import requests
import ast

OK_STATUS = 200

def get_balance_of_account(clientID, alias):

    accounts = get_accounts_from_client(clientID)

    if (account_exists(accounts, alias) == False):
        return None
    
    product = select_product(accounts, alias)
    account_data = get_account_data(product)

    return account_data['monto']



def get_account_data(product):

    url = "https://localhost:5001/api/cuenta-ahorro/" + str(product['productoId'])
    response = requests.get(url, verify=False)

    if (response.status_code != OK_STATUS):
        return {}
    
    response = read_response(response)
    return response['result']


    

def get_accounts_from_client(clientID):

    url = 'https://localhost:5001/api/producto/cliente/' + str(clientID) + '/tipo-producto/1'
    response = requests.get( url, verify=False)

    if (response.status_code != OK_STATUS):
        return []

    response = read_response(response)
    return response['result']


def account_exists(products, alias):
    
    for product in products:

        if ( product['alias'].upper() == alias.upper() ):
            return True

    return False

def select_product(products, alias):
    
    for product in products:

        if ( product['alias'].upper() == alias.upper() ):
            return product

    return {}


def read_response(response):
    byte_str = response.content
    dict_str = byte_str.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)

    return mydata
