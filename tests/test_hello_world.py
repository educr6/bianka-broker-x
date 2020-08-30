import json


def test_index(app, client):

    expected = {'hello': 'world'}

    res = client.get('/')
    
    assert res.status_code == 200
    assert expected == json.loads(res.get_data(as_text=True))