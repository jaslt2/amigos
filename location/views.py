from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from .models import Task, Proposal
from .serializers import UserSerializer, TaskSerializer, ProposalSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer