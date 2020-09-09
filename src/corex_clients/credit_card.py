from .base import CoreXClient
import requests

class CreditCardsCoreXClient (CoreXClient):

    #private variables
    _product_type = '2'

    def __init__(self, api_url, client_id):
        super(CreditCardsCoreXClient, self).__init__(api_url, client_id)


    def get_credit_card_limit(self, alias):

            accounts = self.get_credit_cards_from_client()

            if (self.account_exists(accounts, alias) == False):
                return None
            
            product = self.select_product_by_alias(accounts, alias)
            credit_card_data = self.get_credit_card_data(product)

            return credit_card_data['limiteCredito']

        
    def get_credit_card_available_credit(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product_by_alias(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return credit_card_data['balance']
    

    def get_credit_card_consumed_credit(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product_by_alias(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return ( credit_card_data['limiteCredito'] - credit_card_data['balance'] )



    def get_credit_card_data(self, product):

        url = self.api_url + "/api/tarjeta-credito/" + str(product['productoId'])
        response = requests.get(url, verify=False)

        if (response.status_code != 200):
            return {}
        
        response = self.read_response(response)
        return response['result']
    

    def get_credit_cards_from_client(self):

        url = self.api_url + '/api/producto/cliente/' + str(self.client_id) + '/tipo-producto/' + self._product_type
        response = requests.get( url, verify=False)

        if (response.status_code != 200):
            return []

        response = self.read_response(response)
        return response['result']