from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet)
router.register('groups', views.GroupViewSet)
router.register('users', views.UserViewSet)
router.register('blogposts', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_auth_token/', obtain_auth_token, name='get_auth_token'),
]
