from django.urls import path
from . import views


urlpatterns = [
    path('mixins/', views.TodosListMixinApiView.as_view(),
         name='TodosListMixinApiView'),
    path('mixins/<int:pk>/', views.TodosDetailsMixinApiView.as_view(),
         name='TodosDetailMixinApiView'),

]
