from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views, api

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^api-token-auth/', obtain_jwt_token),
    path(r'^api-token-refresh/', refresh_jwt_token),
]