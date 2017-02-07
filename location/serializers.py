from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, Proposal

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'created_date', 'last_modified', 'proposals', 'status', 'url')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'location', 'mode')

class ProposalSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Proposal
        fields = ('task', 'user', 'created_date', 'last_modified', 'status', 'url')