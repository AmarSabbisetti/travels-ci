from rest_framework.test import APITestCase,APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import User
#from .urls import . 

class UserRegisterTestCase(APITestCase):
    def test_user_register_success(self):
        client = APIClient()
        data = {
            "email": "test1@example.com",
            "password": "password123"
        }
        
        response = client.post('/api/register', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.status_code)
        self.assertTrue(User.objects.filter(email=data["email"]).exists())
        self.assertEqual(response.data['message'], 'USER is created')

    def test_user_register_invalid_data(self):
        client = APIClient()
        data = {
            "email": "test@examdsfaple",
            "password": "password123"
        }

        response = client.post('/api/register', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertFalse(User.objects.filter(email=data.get('email')).exists())


class LoginAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/login' 


        self.user = User.objects.create_user(email='test@example.com', password='password123')


    def test_valid_user_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'password123',

        }
        response = self.client.post(self.url+'/user', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data['token'])
        self.assertEqual(response.data['message'], 'User logged in')

    def test_invalid_user_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.url+'/user', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.data['message'], 'Invalid credentials')

    def test_admin_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'password123',
        }
        response = self.client.post(self.url+'/admin', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.data['message'], 'You are not allowed')

    