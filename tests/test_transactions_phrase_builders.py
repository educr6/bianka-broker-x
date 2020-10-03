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