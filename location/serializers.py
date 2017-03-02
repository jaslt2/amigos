from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, Proposal, Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('longitude', 'latitude')

class UserSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    location = LocationSerializer()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'location', 'mode')

class ProposalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Proposal
        fields = ('task', 'user', 'created_date', 'last_modified', 'status', 'url')

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()
    proposals = ProposalSerializer(many=True)

    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'created_date', 'last_modified', 'proposals', 'status', 'url')

