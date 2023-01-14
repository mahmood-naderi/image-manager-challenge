from http import client
from multiprocessing.connection import Client
from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from users.models import User


@pytest.fixture
def api_client():

    client = APIClient()
    return client

@pytest.fixture
def common_user():

    user = User.objects.create_user(email = 'mahmood@mahmood.com', password = 'qazwsx/1234', is_verified = True)
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_status_200(self, api_client):

        url = reverse('image-manager:image')
        response = api_client.get(url)
        assert response.status_code == 200
