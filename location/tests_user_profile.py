from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .tests_authentication import *

class UserProfileTestCase(AuthenticationTestCase):

	def test_user_profile(self):
		self.register_user()
		key = self.login_user()
		user_id = self.get_user(key)
		self.update_location(key, user_id)
		self.update_mode(key, user_id)

	# GET
	def get_user(self, key):
		url = '/rest-auth/user/'
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		# return id of the current logged in user
		return response.data['pk']

	# PUT
	def update_location(self, key, user_id):
		url = '/users/{}/'.format(user_id)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		data = { 
			"latitude": "100", 
			"longitude": "100"
		}
		response = self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def update_mode(self, key, user_id):
		url = '/users/{}/'.format(user_id)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		data = { 
			"mode": "2"
		}
		response = self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)