from src.phrase_builders import transactions as phrase_builders


def test_trim_transactions1():

    expected = 3
    mock_transactions= [{"transactionID": 1}, {"transactionID": 2}, {"transactionID": 3}, {"transactionID": 4}, {"transactionID": 5}, {"transactionID":5}]

    trimmed_transactions = phrase_builders.trim_transactions(mock_transactions, 3)

    assert expected == len(trimmed_transactions)

def test_trim_transactions2():

    expected = 2
    mock_transactions= [{"transactionID": 1}, {"transactionID": 2}, {"transactionID": 3}, {"transactionID": 4}, {"transactionID": 5}, {"transactionID":6}]

    trimmed_transactions = phrase_builders.trim_transactions(mock_transactions, 2)

    assert expected == len(trimmed_transactions)

def test_get_date_from_transaction_in_phrase1():

    mock_transaction = {"transactionDate": '2020-09-18T20:52:24.897'}
    expected = '18 de septiembre'

    assert expected == phrase_builders.get_date_from_transaction_in_phrase(mock_transaction)

def test_get_date_from_transaction_in_phrase2():

    mock_transaction = {"transactionDate": '2020-07-12T20:52:24.897'}
    expected = '12 de julio'

    assert expected == phrase_builders.get_date_from_transaction_in_phrase(mock_transaction)

def test_get_date_from_transaction_in_phrase3():

    mock_transaction = {"transactionDate": '2020-01-01T20:52:24.897'}
    expected = '1 de enero'

    assert expected == phrase_builders.get_date_from_transaction_in_phrase(mock_transaction)


def create_single_transaction_phrase1():

    mock_transaction = {"transactionDate": '2020-01-01T20:52:24.897', "amount": 15000.0, "description": "Supermercados Bravo"}
    expected = "Supermercados Bravo, en la fecha 1 de enero, por un monto de 15000.0 pesos"

    assert expected == phrase_builders.create_phrase_for_single_transaction(mock_transaction)

def create_single_transaction_phrase2():

    mock_transaction = {"transactionDate": '2020-03-20T20:52:24.897', "amount": 300.0, "description": "Amazon"}
    expected = "Amazon, en la fecha 20 de marzo, por un monto de 300.0 pesos"

    assert expected == phrase_builders.create_phrase_for_single_transaction(mock_transaction)


