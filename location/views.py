from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from .models import Task, Proposal
from .serializers import *

# ViewSets define the view behavior.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return NewTaskSerializer
        return TaskSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NewProposalSerializer
        elif self.request.method == 'PUT':
        	return UpdateProposalSerializer
        return ProposalSerializer