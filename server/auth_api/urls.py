from django.urls import include, path

from . import views, api

urlpatterns = [
    path('', views.index, name='index'),
]