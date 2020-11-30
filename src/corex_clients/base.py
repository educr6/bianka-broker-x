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

    def __init__(self, api_url, client_id, auth_header):
        self.api_url = api_url
        self.client_id = client_id
        self.auth_header = auth_header


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

        product_alias = product_alias.lower()
        search_alias = search_alias.lower()

        product_alias = self.remove_tildes(product_alias)
        search_alias  = self.remove_tildes(search_alias)

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
        response = requests.get(url, verify=False, headers=self.auth_header)

        if (response.status_code != 200):
            return []
        
        response = self.read_response(response)
        return response

    
    def get_beneficiary_product(self, beneficiary_alias):

        beneficiary_list = self.get_beneficiary_list()

        if (beneficiary_list == []):
            return {}
        
        for beneficiary in beneficiary_list:

            if ( self.is_alias_same(beneficiary["alias"], beneficiary_alias) ):
                return beneficiary["product"]
        
        return {} 
            

        
    

    def get_beneficiary_list(self):
        
        url = self.api_url + "/api/beneficiary/client/%s" % str(self.client_id)
        response = requests.get(url, verify=False)

      

        if (response.status_code != 200):
            return []
        
        response = self.read_response(response)
        return response


    
    def remove_tildes(self, alias):

        new_alias = alias.replace("á", "a")
        new_alias = new_alias.replace("é", "e")
        new_alias = new_alias.replace("í", "i")
        new_alias = new_alias.replace("ó", "o")
        new_alias = new_alias.replace("ú", "u")

        return new_alias
        





        
    


    def read_response(self, response):
        return json.loads(response.content)
    
    def read_response2(self, response):
        return json.loads(response)

        