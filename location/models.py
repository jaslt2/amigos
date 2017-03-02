from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from enum import Enum

class TaskStatus(Enum):
	OPEN = 1
	ACCEPTED = 2
	RESOLVED = 3
	CANCELLED = 4

class ProposalStatus(Enum):
	OPEN = 1
	ACCEPTED = 2
	REJECTED = 3

class Mode(Enum):
	PRIVATE = 1
	HELP_NEEDED = 2

class Location(models.Model):
	user = models.OneToOneField(User, related_name='location')
	longitude = models.DecimalField(max_digits=8, decimal_places=3)
	latitude = models.DecimalField(max_digits=8, decimal_places=3)

class UserMode(models.Model):
	user = models.OneToOneField(User, related_name='mode')
	mode = models.CharField(choices=[(choice.value, choice.name.replace("_", " ")) for choice in Mode], max_length=1, default=Mode.PRIVATE)

class Task(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=[(choice.value, choice.name.replace("_", " ")) for choice in TaskStatus], max_length=1, default=TaskStatus.OPEN)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Proposal(models.Model):
	task = models.ForeignKey(Task, related_name='proposals', default=None)
	user = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(default=timezone.now)
	last_modified = models.DateTimeField(default=timezone.now)
	status = models.CharField(choices=[(choice.value, choice.name.replace("_", " ")) for choice in ProposalStatus], max_length=50, default=ProposalStatus.OPEN)


