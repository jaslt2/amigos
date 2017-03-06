from rest_framework import status
from rest_framework.test import APITestCase

# Register a new user
class UserProfileTestCase(APITestCase):

	def test_register_user(self):
		url = '/rest-auth/registration/'
		data = { 
			"username": "admin1", 
			"email": "admin1@admin.com", 
			"password1": "adminPassw0rd", 
			"password2": 
			"adminPassw0rd" 
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
