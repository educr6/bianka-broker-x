from datetime import datetime

def create_transaction_phrase(transactions_list, number_of_transactions):

    complete_phrase = ""
    initial_phrase = "Estas son sus ultimas %s transacciones: " % number_of_transactions

    selected_transactions = trim_transactions(transactions_list, number_of_transactions)
    transaction_phrases = group_transaction_phrases(selected_transactions)

    complete_phrase = initial_phrase + "\n" + transaction_phrases

    return complete_phrase



 

months_in_spanish = {1: "enero", 2: "febrero", 3: "marzo", 
4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8:"agosto",
 9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}


def trim_transactions(transaction_list, number_of_transactions):
    return transaction_list[:number_of_transactions]

def create_phrase_for_single_transaction(transaction):

    date = get_date_from_transaction_in_phrase(transaction)
    amount = transaction["amount"]
    description = transaction["description"]

    phrase = "%s, en la fecha %s, por un monto de %s pesos." % (description, date, amount)
    return phrase


def get_date_from_transaction_in_phrase(transaction):

    date_string = transaction["transactionDate"].split('T')[0]
    dt_object = datetime.strptime(date_string, '%Y-%m-%d')

    date_phrase = "%s de %s" % (dt_object.day, months_in_spanish[dt_object.month])

    return date_phrase



def group_transaction_phrases(transactions):

    grouped_transactions_phrase = ""

    for transaction in transactions:
        phrase = create_phrase_for_single_transaction(transaction)
        grouped_transactions_phrase += phrase
        grouped_transactions_phrase += "\n"
    
    return grouped_transactions_phrase

