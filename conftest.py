import pytest
from rest_framework.test import APIClient
from accounts.models import User
from companies.models import Company

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_factory(db):
    def create_user(**kwargs):
        return User.objects.create_user(
            username=kwargs.get("username", "testuser"),
            email=kwargs.get("email", "test@example.com"),
            password=kwargs.get("password", "password123")
        )
    return create_user

@pytest.fixture
def company_factory(db):
    def create_company(**kwargs):
        company = Company.objects.create(
            company_name=kwargs.get("company_name", "Test Company"),
            company_email=kwargs.get("company_email", "test@company.com"),
            company_address=kwargs.get("company_address", ""),
            company_phone=kwargs.get("company_phone", "")
        )
        if users := kwargs.get("users"):
            company.users.set(users)
        return company
    return create_company
