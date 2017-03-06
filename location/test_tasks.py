from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .tests import *

class TaskTestCase(AuthenticationTestCase):

	def test_task(self):
		self.register_user()
		key = self.login_user()
		self.create_task(key)

	def create_task(self, key):
		url = '/tasks/'
		data = { 
			"title": "Help me get home", 
			"description": "I need help getting back to my flat in West London", 
		}
		print("Authenticating with key " + key)
		# put the token in the Authorization header
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.post(url, data)
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)