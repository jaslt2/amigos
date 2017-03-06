from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import ChoiceEnum
from django.db.models.signals import post_save
from django.dispatch import receiver

class TaskStatus(ChoiceEnum):
	OPEN = 1
	ACCEPTED = 2
	RESOLVED = 3
	CANCELLED = 4

class ProposalStatus(ChoiceEnum):
	OPEN = 1
	ACCEPTED = 2
	REJECTED = 3

class Mode(ChoiceEnum):
	PRIVATE = 1
	HELP_NEEDED = 2

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Location(BaseModel):
	longitude = models.DecimalField(max_digits=8, decimal_places=3)
	latitude = models.DecimalField(max_digits=8, decimal_places=3)

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    location = models.OneToOneField(Location, blank=True, null=True)
    mode = models.IntegerField(choices=Mode.choices(), default=1, blank=True)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    # 	instance.user_profile.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	        Profile.objects.create(user=instance)

class Task(BaseModel):
    userProfile = models.ForeignKey(Profile)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=TaskStatus.choices(), default=1, blank=True)

    def __str__(self):
        return self.title

class Proposal(BaseModel):
	task = models.ForeignKey(Task, related_name='proposals', default=None)
	userProfile = models.ForeignKey(Profile)
	status = models.IntegerField(choices=ProposalStatus.choices(), default=1, blank=True)


