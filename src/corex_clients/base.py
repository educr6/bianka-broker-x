import requests
import ast
import json



class CoreXClient:

    api_url = ''
    client_id = ''
    product_type_enum = {
        "SavingsAccount": 1,
        "CreditCard": 2
    }

    def __init__(self, api_url, client_id):
        self.api_url = api_url
        self.client_id = client_id


    def account_exists(self, products, alias):
        
        for product in products:

            if ( self.is_alias_same(product['alias'], alias) ):
                return True

        return False
        

    def select_product_by_alias(self, products, alias):
        
        for product in products:

            if ( self.is_alias_same(product['alias'], alias) ):
                return product

        return {}
    
    def is_alias_same(self, product_alias, search_alias):

        product_alias = product_alias.upper()
        search_alias = search_alias.upper()

        if ( product_alias == search_alias ):
            return True
        
        if ( search_alias in product_alias ):
            return True
        
        return False
    
    def translate_product_type(self, product_type):
        
        if (product_type in self.product_type_enum):
            return self.product_type_enum[product_type]
        
        return 0
    
    def get_product_transactions(self, product):

        
        url = self.api_url + '/api/historical-transaction/product/%s' % str(product["productId"])
        response = requests.get(url, verify=False)

        if (response.status_code != 200):
            return []
        
        response = self.read_response(response)
        return response
        

        
    


    def read_response(self, response):
        return json.loads(response.content)
    
    def read_response2(self, response):
        return json.loads(response)

        