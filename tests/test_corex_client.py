def test_read_response2(corex_client):

    expected = {'hello': 'world'}
    
    assert expected == corex_client.read_response2(b'{\'hello\': \'world\'}')