from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosViewSetApiView, basename='viewsets')


urlpatterns = [
    # path('generics/', views.TodosGenericApiView.as_view(),
    #      name='TodosGenericApiView'),
    # path('generics/<int:pk>/', views.TodosGenericDetailsApiView.as_view(),
    #      name='TodosGenericDetailsApiView'),
    path('viewsets/', include(router.urls)),
    path('users/', views.UserGenericApiView.as_view(), name='UserGenericApiView'),
]
