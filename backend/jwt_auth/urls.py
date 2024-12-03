from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from drf_yasg.utils import swagger_auto_schema
from jwt_auth import views

login_view = swagger_auto_schema('POST', tags=['auth'])(token_obtain_pair)
refresh_token_view = swagger_auto_schema('POST', tags=['auth'])(token_refresh)

urlpatterns = [
    path('user/login/', login_view, name='user-login'),
    path('user/refresh-token/', refresh_token_view, name='refresh-token'),
    path(
        'user/register/',
        views.RegisterUserAPIView.as_view(),
        name='register-user',
    ),
    path('user/info/', views.UserInfoAPIView.as_view(), name='user-info'),
]
