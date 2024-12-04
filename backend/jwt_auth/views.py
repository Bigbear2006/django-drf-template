from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from jwt_auth.models import User
from jwt_auth.serializers import UserSerializer


@method_decorator(swagger_auto_schema(tags=['auth']), 'post')
class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(swagger_auto_schema(tags=['auth']), 'get')
class UserInfoAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
