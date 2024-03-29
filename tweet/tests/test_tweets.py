from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import pytest

# Create your tests here.


@pytest.mark.django_db
class TestCreateTweet:
    def test_that_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_authenticated_returns_201(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_201_CREATED


