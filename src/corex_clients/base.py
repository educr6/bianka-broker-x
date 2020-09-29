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

            if ( product['alias'].upper() == alias.upper() ):
                return True

        return False

    def select_product_by_alias(self, products, alias):
        
        for product in products:

            if ( product['alias'].upper() == alias.upper() ):
                return product

        return {}


    def read_response(self, response):
        return json.loads(response.content)
    
    def read_response2(self, response):
        return json.loads(response)

        