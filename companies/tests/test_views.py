import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_create_company(user_factory):
    user = user_factory()
    client = APIClient()
    client.force_authenticate(user)

    url = reverse("company-list")  # DRF router name
    data = {
        "company_name": "Test Inc.",
        "company_email": "test@inc.com",
        "users": [user.id]
    }

    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["company_name"] == "Test Inc."
