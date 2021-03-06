from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class NewLocationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Location(**validated_data)

    class Meta:
        model = Location
        fields = ('longitude', 'latitude')

class LocationSerializer(serializers.ModelSerializer):
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Location(**validated_data)

    class Meta:
        model = Location
        fields = ('created_date','last_modified','longitude', 'latitude')

class UserSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id','url', 'username')

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
        fields = ('created_date','last_modified','id','location', 'mode', 'user')

class UpdateProfileSerializer(serializers.ModelSerializer):
    location = NewLocationSerializer(required=False)
    mode = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location', None)
        if location_data:
            location = Location.objects.get_or_create(**location_data)[0]
            instance.location = location
        instance.mode = validated_data.get('mode', instance.mode)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = ('location', 'mode')

class TaskIdField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        return Task.objects.filter(id=data)

class UpdateProposalSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()

    class Meta:
        model = Proposal
        fields = ('status',)

class NewProposalSerializer(serializers.ModelSerializer):
    task = TaskIdField(queryset=Task.objects.all())
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        taskId = validated_data['task']
        validated_data['task'] = Task.objects.filter(id=taskId)[0]
        currentUser = self.context['request'].user
        profile = Profile.objects.filter(user=currentUser).get()  
        validated_data['userProfile'] = profile
        return Proposal.objects.create(**validated_data)

    class Meta:
        model = Proposal
        fields = ('task', 'id')

class ProposalSerializer(serializers.ModelSerializer):
    userProfile = ProfileSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()

    class Meta:
        model = Proposal
        fields = ('id','task', 'userProfile', 'created_date', 'last_modified', 'status', 'url')

class NewTaskSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        currentUser = self.context['request'].user
        profile = Profile.objects.filter(user=currentUser).get()  
        validated_data['userProfile'] = profile
        return Task.objects.create(**validated_data)

    class Meta:
        model = Task
        fields = ('title', 'description','id')

class TaskSerializer(serializers.ModelSerializer):
    userProfile = ProfileSerializer()
    created_date = serializers.ReadOnlyField()
    last_modified = serializers.ReadOnlyField()
    proposals = ProposalSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id','userProfile', 'title', 'description', 'created_date', 'last_modified', 'proposals', 'status', 'url')