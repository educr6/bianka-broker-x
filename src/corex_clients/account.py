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

        return account_data['amount']
    

    def get_accounts_from_client(self):

        url = self.api_url + '/api/product/client/' + str(self.client_id) + '/product-type/' + str(self._product_type)
        response = requests.get( url, verify=False)

        if (response.status_code != 200):
            return []

        response = self.read_response(response)
        return response


    
    def get_account_data(self, product):

        url = self.api_url + "/api/savings-account/" + str(product['productId'])
        response = requests.get(url, verify=False)

        if (response.status_code != 200):
            return {}
        
        response = self.read_response(response)
        return response
    
    def get_account_transactions(self, alias):

        accounts = self.get_accounts_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        account = self.select_product_by_alias(accounts, alias)


        transactions = self.get_product_transactions(account)
        return transactions
    
    def transfer_money_to_beneficiary(self, transfer_petition):
        return {}




