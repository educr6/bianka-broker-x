def test_read_response2(credit_card_corex_client):

    expected = {'hello': 'world'}
    assert expected == credit_card_corex_client.read_response2(b'{\"hello\": \"world\"}')