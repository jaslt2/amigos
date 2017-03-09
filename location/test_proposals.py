from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .test_tasks import *

class TaskTestCase(TaskTestCase):

	def test_proposal(self):
		self.register_user()
		key = self.login_user()
		taskId = self.create_task(key)
		proposalId = self.create_proposal(key, taskId)
		self.accept_proposal(key, proposalId)
		proposalId = self.create_proposal(key, taskId)
		self.reject_proposal(key, proposalId)


	# POST to create a proposal against an OPEN task
	def create_proposal(self, key, taskId):
		url = '/proposals/'
		# body is the task id
		data = { 
			"task" : taskId
		}
		# put the token in the Authorization header
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.post(url, data)
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		return response.data['id']

	# PUT to update the state of a proposal to accept it
	def accept_proposal(self, key, proposalId):
		# e.g. /proposals/1
		url = '/proposals/{}/'.format(proposalId)
		# body is the task id
		# status 2 is ACCEPTED
		data = { 
			"status" : "2"
		}
		# put the token in the Authorization header
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.put(url, data)
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# PUT to update the state of a proposal to reject it
	def reject_proposal(self, key, proposalId):
		# e.g. /proposals/1
		url = '/proposals/{}/'.format(proposalId)
		# body is the task id
		# status 3 is REJECTED
		data = { 
			"status" : "3"
		}
		# put the token in the Authorization header
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + key)
		response = self.client.put(url, data)
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)