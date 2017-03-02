from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class LocationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Location(**validated_data)

    class Meta:
        model = Location
        fields = ('longitude', 'latitude')

class UserSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('url', 'username')
        
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()
    mode = serializers.IntegerField(required=False)

    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        if location_data:
            location = Location.objects.get_or_create(**location_data)[0]
            validated_data['location'] = location
        return Profile.objects.create(**validated_data)

    class Meta:
        model = Profile
        fields = ('location', 'mode', 'user')

class ProposalSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Proposal
        fields = ('task', 'user', 'created_date', 'last_modified', 'status', 'url')

class TaskSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()
    proposals = ProposalSerializer(many=True)

    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'created_date', 'last_modified', 'proposals', 'status', 'url')