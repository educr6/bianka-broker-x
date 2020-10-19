from .base import CoreXClient
from src.phrase_builders import transactions as transphraseBuilder
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
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

            return credit_card_data['creditLimit']
    
    def get_missing_days(self, alias):
            accounts = self.get_credit_cards_from_client()

            if (self.account_exists(accounts, alias) == False):
                return None
            
            product = self.select_product_by_alias(accounts, alias)
            credit_card_data = self.get_credit_card_data(product)

            cutDate = credit_card_data['cutDate']
            daysLimitPayment = credit_card_data['daysLimitPayment']

            date_string = cutDate.split('T')[0]
            dt_object = datetime.strptime(date_string, '%Y-%m-%d')
            
            currentDate = datetime.now()
            newCutDate = self.get_cut_date(dt_object, daysLimitPayment,  currentDate)
            return (newCutDate - currentDate).days


    def get_cut_date(self, cutDate, daysLimitPayment, currentDate):
        diferenceMonths = self.get_month_between_two_date(cutDate, currentDate)
        newCutDate = cutDate + relativedelta(months=diferenceMonths)
        newCutDate = newCutDate + timedelta(days=daysLimitPayment)

        totaldays = (newCutDate - currentDate).days

        if (totaldays < 0):
            return newCutDate + relativedelta(months=1)
        else:
            return newCutDate


    def get_month_between_two_date(self, start_date, end_date):
        return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    
        
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

        return ( credit_card_data['creditLimit'] - credit_card_data['balance'] )
    

    def get_credit_card_minimum_payment(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product_by_alias(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return credit_card_data['minimumPayment']
    

    def get_credit_card_cut_payment(self, alias):

        accounts = self.get_credit_cards_from_client()

        if (self.account_exists(accounts, alias) == False):
            return None
        
        product = self.select_product_by_alias(accounts, alias)
        credit_card_data = self.get_credit_card_data(product)

        return credit_card_data['cutPayment']



    def get_credit_card_data(self, product):

        url = self.api_url + "/api/credit-card/" + str(product['productId'])
        response = requests.get(url, verify=False)

        if (response.status_code != 200):
            return {}
        
        response = self.read_response(response)
        return response
    

    def get_credit_cards_from_client(self):

        url = self.api_url + '/api/product/client/' + str(self.client_id) + '/product-type/' + self._product_type
        response = requests.get( url, verify=False)

        if (response.status_code != 200):
            return []

        response = self.read_response(response)
        return response


    
    def get_credit_card_transactions(self, alias):

        credit_cards = self.get_credit_cards_from_client()

        if (self.account_exists(credit_cards, alias) == False):
            return None
        
        card = self.select_product_by_alias(credit_cards, alias)


        transactions = self.get_product_transactions(card)
        return transactions
