import pytest
from django.urls import reverse
from accounts.models import User

@pytest.mark.django_db
def test_user_list_view(api_client, user_factory):
    user_factory(username="user1")
    user_factory(username="user2")

    url = reverse("user-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse("user-list")
    payload = {
        "username": "newuser",
        "password": "securepassword123"
    }

    response = api_client.post(url, payload)

    assert response.status_code == 201
    assert User.objects.filter(username="newuser").exists()
