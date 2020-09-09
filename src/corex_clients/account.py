from .base import CoreXClient
import requests

class AccountsCoreXClient (CoreXClient):

    #private variables
    _product_type = '1'

    def __init__(self, api_url, client_id):
        super(AccountsCoreXClient, self).__init__(api_url, client_id)
    

    def get_balance_of_account(self, alias):

        accounts = self.get_accounts_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product_by_alias(accounts, alias)
        account_data = self.get_account_data(product)

        return account_data['monto']
    

    def get_accounts_from_client(self):

        url = self.api_url + '/api/producto/cliente/' + str(self.client_id) + '/tipo-producto/' + str(self._product_type)
        response = requests.get( url, verify=False)

        if (response.status_code != 200):
            return []

        response = self.read_response(response)
        return response['result']


    
    def get_account_data(self, product):

        url = self.api_url + "/api/cuenta-ahorro/" + str(product['productoId'])
        response = requests.get(url, verify=False)

        if (response.status_code != 200):
            return {}
        
        response = self.read_response(response)
        return response['result']
    




