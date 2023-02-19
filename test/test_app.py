

def test_post_message(test_client, init_database):
    response = test_client.post('/messages', json={'message': 'Test message'})
    assert response.status_code == 201


def test_get_messages(test_client, init_database):
    response = test_client.get('/messages')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['message'] == 'Test message'

def test_generate_token(test_client, init_database):
    response = test_client.get('/token')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
