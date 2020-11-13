from .base import CoreXClient
import requests
import json

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

    
    def get_account_by_alias(self, alias):
        
        accounts = self.get_accounts_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        account = self.select_product_by_alias(accounts, alias)
        return account

    
    def transfer_money_to_beneficiary(self, transfer_petition):

        sourceProduct = self.get_account_by_alias(transfer_petition["accountAlias"])

        if (sourceProduct == None):
            return {
                "success":  False,
                "message": "No pudimos encontrar entre sus cuentas la titulada %s" % transfer_petition["accountAlias"]
            }
        
        beneficiaryProduct = self.get_beneficiary_product(transfer_petition["beneficiary"])

        if (beneficiaryProduct == {}):
            return {
                "success":  False,
                "message": "No pudimos encontrar entre sus beneficiarios a %s" % transfer_petition["beneficiary"]
            }
        
       
        data = {
            "productSourceId": sourceProduct["productId"],
            "productTargetId": beneficiaryProduct["productId"],
            "amount": transfer_petition["amount"],
            "note": "Esta transferencia se hizo a traves de Bianka"
        }

        url = self.api_url + "/api/transaction"

        response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"}, verify=False)


        if (response.status_code != 200) :
            return {
                "success": False,
                "message": "Hubo un error al intentar la transaccion"
            }
        

        response = self.read_response(response)

        result = {"success": True, "message": "Transaccion sometida"}
        result.update(response)

        return result
    


    def transfer_money_between_own_accounts(self, transfer_petition):

        sourceProduct = self.get_account_by_alias(transfer_petition["sourceAccountAlias"])

        if (sourceProduct == None):
            return {
                "success":  False,
                "message": "No pudimos encontrar entre sus cuentas la titulada %s" % transfer_petition["sourceAccountAlias"]
            }
        
        targetProduct = self.get_account_by_alias(transfer_petition["targetAccountAlias"])

        if (targetProduct == {}):
            return {
                "success":  False,
                "message": "No pudimos encontrar entre sus cuentas la titulada %s" % transfer_petition["targetAccountAlias"]
            }
        
       
        data = {
            "productSourceId": sourceProduct["productId"],
            "productTargetId": targetProduct["productId"],
            "amount": transfer_petition["amount"],
            "note": "Esta transferencia se hizo a traves de Bianka"
        }

        url = self.api_url + "/api/transaction"

        response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"}, verify=False)


        if (response.status_code != 200) :
            return {
                "success": False,
                "message": "Hubo un error al intentar la transaccion"
            }
        

        response = self.read_response(response)

        result = {"success": True, "message": "Transaccion sometida"}
        result.update(response)

        return result

    
    def complete_transfer_to_beneficiary(self, complete_transfer_petition):

        operation_id = complete_transfer_petition["operation_id"]
        key = complete_transfer_petition["key"]

        url = self.api_url + "/api/transaction/rowuid/%s/key/%s" % (operation_id, key)
        response = requests.post(url, data={}, verify=False)

        response_content = self.read_response(response)

        if(response.status_code != 200):

            print ("EL FALLO SE VE DE ESTA FORMA", response_content)

            return {
                "success": False,
                "message": response_content["Message"]
            }
        

        return {"success": True}


        


           




