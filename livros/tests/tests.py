import pytest
from django.urls import reverse

from biblioteca.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse("api:livro"))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_urls(resp):
    assert_contains(resp, "livros")
