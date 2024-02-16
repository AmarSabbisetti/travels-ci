
from rest_framework.test import APITestCase
#from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from users.models import User
#from packages

class PackagesAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='password123')
        self.admin = User.objects.create_superuser(email='admin@example.com', password='adminpassword')
        self.packages_list_url = '/api/packages/'
        self.package_detail_url = '/api/packages/1'
        refresh = RefreshToken.for_user(self.admin)
        self.admin_token = str(refresh.access_token)
        #print(self.admin_token)


    def test_create_package(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.admin_token)
        
        data = {
            "name":"dskjfgi",
            "description":"akdsgjfjlak",
            "days":3,
            "price":250,
            "start_date":"2024-02-16",
            "end_date":"2024-02-20",
            "slots":100
            }
        response = self.client.post(self.packages_list_url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_packages(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.admin_token)
        response = self.client.get(self.packages_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_unauthenticated_access(self):
        
        response = self.client.get(self.packages_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.admin_token)
        response = self.client.post(self.packages_list_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
