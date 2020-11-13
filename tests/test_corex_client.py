

def test_read_response2(base_corex_client):

    expected = {'hello': 'world'}
    assert expected == base_corex_client.read_response2(b'{\"hello\": \"world\"}')

def test_account_exists1(base_corex_client):

    mock_product_set = [{"productID": 1, "alias": "Ahorros"}, {"productID": 2, "alias": "Platinum"}, {"productID": 3, "alias": "Oro"}]
    product_to_be_searched = {"productID": 1, "alias": "Ahorros"}

    expected_answer = True
    assert base_corex_client.account_exists(mock_product_set, product_to_be_searched["alias"] ) == expected_answer

def test_account_exists2(base_corex_client):

    mock_product_set = [{"productID": 1, "alias": "Ahorros"}, {"productID": 2, "alias": "Platinum"}, {"productID": 3, "alias": "Oro"}]
    product_to_be_searched = {"productID": 1, "alias": "ahorros"}

    expected_answer = True
    assert base_corex_client.account_exists(mock_product_set, product_to_be_searched["alias"] ) == expected_answer

def test_account_exists3(base_corex_client):

    mock_product_set = [{"productID": 1, "alias": "Ahorros"}, {"productID": 2, "alias": "Platinum"}, {"productID": 3, "alias": "Oro"}]
    product_to_be_searched = {"productID": 1, "alias": "Infinite"}

    expected_answer = False
    assert base_corex_client.account_exists(mock_product_set, product_to_be_searched["alias"] ) == expected_answer


def test_select_product_by_alias1(base_corex_client):

    mock_product_set = [{"productID": 1, "alias": "Ahorros"}, {"productID": 2, "alias": "Platinum"}, {"productID": 3, "alias": "Oro"}]
    product_to_be_searched = {"productID": 1, "alias": "Ahorros"}

    expected_answer = product_to_be_searched
    assert base_corex_client.select_product_by_alias(mock_product_set, product_to_be_searched["alias"] ) == expected_answer

def test_select_product_by_alias2(base_corex_client):

    mock_product_set = [{"productID": 1, "alias": "Ahorros"}, {"productID": 2, "alias": "Platinum"}, {"productID": 3, "alias": "Oro"}]
    product_to_be_searched = {"productID": 4, "alias": "Infinite"}

    expected_answer = {}
    assert base_corex_client.select_product_by_alias(mock_product_set, product_to_be_searched["alias"] ) == expected_answer


def test_is_alias_same(base_corex_client):

    product_alias = "Ahorros"
    search_alias = "Ahorros"

    expected_answer = True

    assert base_corex_client.is_alias_same(product_alias, search_alias) == expected_answer


def test_is_alias_same2(base_corex_client):

    product_alias = "Ahorros"
    search_alias = "ahorros"

    expected_answer = True

    assert base_corex_client.is_alias_same(product_alias, search_alias) == expected_answer

def test_is_alias_same3(base_corex_client):

    product_alias = "Ahorros"
    search_alias = "ahorro"

    expected_answer = True

    assert base_corex_client.is_alias_same(product_alias, search_alias) == expected_answer

def test_is_alias_same4(base_corex_client):

    product_alias = "Ahorros"
    search_alias = "Infinite"

    expected_answer = False

    assert base_corex_client.is_alias_same(product_alias, search_alias) == expected_answer

def test_is_alias_same5(base_corex_client):

    product_alias = "Nomina"
    search_alias = "nómina"

    expected_answer = True

    assert base_corex_client.is_alias_same(product_alias, search_alias) == expected_answer


def test_corex_client_product_type_detection1(base_corex_client):

    productType = "SavingsAccount"
    expected = 1

    assert expected == base_corex_client.translate_product_type(productType)

def test_corex_client_product_type_detection2(base_corex_client):

    productType = "CreditCard"
    expected = 2

    assert expected == base_corex_client.translate_product_type(productType)

def test_corex_client_product_type_detection3(base_corex_client):

    productType = "CreditCards"
    expected = 0

    assert expected == base_corex_client.translate_product_type(productType)

def test_corex_client_product_type_detection4(base_corex_client):

    productType = "SavingAccount"
    expected = 0

    assert expected == base_corex_client.translate_product_type(productType)

