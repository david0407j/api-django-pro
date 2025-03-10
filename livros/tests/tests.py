import pytest
from django.urls import reverse
from rest_framework import status


@pytest.fixture
def resp(client, db):
    url = reverse("livro-list-create")
    return client.get(url)


@pytest.mark.django_db
def test_status_code(resp):
    assert resp.status_code == status.HTTP_200_OK


def test_urls(resp):
    assert "[]" in resp.content.decode()
