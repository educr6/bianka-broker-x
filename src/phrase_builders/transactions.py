from datetime import datetime
#def create_transaction_phrase(transactions, number_of_transactions):
 #   return
   # selected_transactions = transactions[:]

months_in_spanish = {1: "enero", 2: "febrero", 3: "marzo", 
4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8:"agosto",
 9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}


def trim_transactions(transaction_list, number_of_transactions):
    return transaction_list[:number_of_transactions]

def create_phrase_for_single_transaction(transaction):

    phrase = "%s, en la fecha %s, por un monto de %s pesos" % ("uan", "two", "three")
    return phrase

def get_date_from_transaction_in_phrase(transaction):

    date_string = transaction["transactionDate"].split('T')[0]
    dt_object = datetime.strptime(date_string, '%Y-%m-%d')

    date_phrase = "%s de %s" % (dt_object.day, months_in_spanish[dt_object.month])

    return date_phrase



