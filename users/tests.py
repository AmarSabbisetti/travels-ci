
# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class UserRegisterTestCase(TestCase):
    def test_user_register(self):
        client = APIClient()
        url = reverse('user-register')
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginTestCase(TestCase):
    def test_user_login(self):
        client = APIClient()
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

class BlacklistTokenUpdateViewTestCase(TestCase):
    def test_blacklist_token_update_view(self):
        client = APIClient()
        url = reverse('blacklist-token-update')
        data = {'refresh_token': 'refresh_token_here'}
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

class UserPackageViewSetTestCase(TestCase):
    def test_user_package_list(self):
        client = APIClient()
        client.force_authenticate(user=user_instance)  # Assuming you have a user instance for testing
        url = reverse('user-package-list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_package_retrieve(self):
        client = APIClient()
        client.force_authenticate(user=user_instance)  # Assuming you have a user instance for testing
        url = reverse('user-package-detail', args=[1])  # Assuming the PK is 1
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
