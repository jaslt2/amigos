from django.contrib import admin
from .models import Task, Location

# Register your models here.
admin.site.register(Task);
admin.site.register(Location)