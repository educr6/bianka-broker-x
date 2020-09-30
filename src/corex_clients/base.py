import requests
import ast
import json



class CoreXClient:

    api_url = ''
    client_id = ''

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




    def read_response(self, response):
        return json.loads(response.content)
    
    def read_response2(self, response):
        return json.loads(response)

        