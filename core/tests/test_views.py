from http import HTTPStatus
from django.shortcuts import resolve_url


def test_list_all_authors(client):
    response = client.get(resolve_url('core:list-authors'))

    assert response.status_code == HTTPStatus.OK
