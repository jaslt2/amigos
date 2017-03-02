from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Task);
admin.site.register(Location);
admin.site.register(Proposal);
admin.site.register(Profile);