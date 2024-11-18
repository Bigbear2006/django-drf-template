from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from . import views

urlpatterns = [
    path('user/login/', token_obtain_pair, name='user-login'),
    path('user/refresh-token/', token_refresh, name='refresh-token'),
    path('user/register/', views.RegisterUserAPIView.as_view(), name='register-user'),
    path('user/info/', views.UserInfoAPIView.as_view(), name='user-info'),
]
