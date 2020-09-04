import requests
import ast

OK_STATUS = 200


class CoreXClient:

    api_url = ''
    client_id = ''

    def __init__(self, api_url, client_id):
        self.api_url = api_url
        self.client_id = client_id


    def get_balance_of_account(self, alias):

        accounts = self.get_accounts_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product(accounts, alias)
        account_data = self.get_account_data(product)

        return account_data['monto']
    

    def get_credit_card_limit(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return credit_card_data['limiteCredito']

    
    def get_credit_card_available_credit(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return credit_card_data['balance']



    def get_credit_card_data(self, product):

        url = self.api_url + "/api/tarjeta-credito/" + str(product['productoId'])
        response = requests.get(url, verify=False)

        if (response.status_code != OK_STATUS):
            return {}
        
        response = self.read_response(response)
        return response['result']

    
    def get_account_data(self, product):

        url = self.api_url + "/api/cuenta-ahorro/" + str(product['productoId'])
        response = requests.get(url, verify=False)

        if (response.status_code != OK_STATUS):
            return {}
        
        response = self.read_response(response)
        return response['result']


        

    def get_accounts_from_client(self):

        url = self.api_url + '/api/producto/cliente/' + str(self.client_id) + '/tipo-producto/1'
        response = requests.get( url, verify=False)

        if (response.status_code != OK_STATUS):
            return []

        response = self.read_response(response)
        return response['result']
    

    def get_credit_cards_from_client(self):

        url = self.api_url + '/api/producto/cliente/' + str(self.client_id) + '/tipo-producto/2'
        response = requests.get( url, verify=False)

        if (response.status_code != OK_STATUS):
            return []

        response = self.read_response(response)
        return response['result']


    def account_exists(self, products, alias):
        
        for product in products:

            if ( product['alias'].upper() == alias.upper() ):
                return True

        return False

    def select_product(self, products, alias):
        
        for product in products:

            if ( product['alias'].upper() == alias.upper() ):
                return product

        return {}


    def read_response(self, response):
        byte_str = response.content
        dict_str = byte_str.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        return mydata
    
    def read_response2(self, response):
        byte_str = response
        dict_str = byte_str.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        return mydata
