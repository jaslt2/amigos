from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

from .views import UserViewSet,TaskViewSet, ProposalViewSet

swagger_view = get_swagger_view(title='Amigos API')

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'proposals', ProposalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger/', swagger_view)
]



