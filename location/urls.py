from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

from .views import *

swagger_view = get_swagger_view(title='Amigos API')

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'proposals', ProposalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^swagger/', swagger_view)
]



