from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .tests_authentication import *

class TaskTestCase(AuthenticationTestCase):

	def test_task(self):
		self.register_user()
		key = self.login_user()
		taskId = self.create_task(key)
		self.update_task(key, taskId)
		self.get_task(key, taskId)

	# POST
	def create_task(self, key):
		url = '/tasks/'
		data = { 
			"title": "Help me get home", 
			"description": "I need help getting back to my flat in West London"
		}
		# put the token in the Authorization header, e.g. Authorization: Token 123445452423
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		return response.data['id']

	# PUT
	def update_task(self, key, taskId):
		# e.g. /tasks/1
		url = '/tasks/{}/'.format(taskId)
		data = { 
			"title": "Help me get home (updated)", 
			"description": "I need help getting back to my flat in West London (updated)"
		}
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# GET
	def get_task(self, key, taskId):
		# e.g. /tasks/1
		url = '/tasks/{}/'.format(taskId)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)