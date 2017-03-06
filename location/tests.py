from rest_framework import status
from rest_framework.test import APITestCase

class AuthenticationTestCase(APITestCase):

	def test_auth(self):
		self.register_user()
		self.login_user()
		self.password_change()
		self.logout_user()

	def register_user(self):
		url = '/rest-auth/registration/'
		data = { 
			"username": "testUser", 
			"email": "test@test.com", 
			"password1": "testPassw0rd", 
			"password2": "testPassw0rd" 
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def login_user(self):
		url = '/rest-auth/login/'
		data = { 
			"username": "testUser", 
			"email": "test@test.com", 
			"password": "testPassw0rd" 
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		return response.data['key']

	def password_change(self):
		url = '/rest-auth/password/change/'
		data = {
		    "new_password1": "testPassw0rd1",
		    "new_password2": "testPassw0rd1"
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def logout_user(self):
		url = '/rest-auth/logout/'
		data = {}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)	