from http import HTTPStatus


def test_root_return_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}
