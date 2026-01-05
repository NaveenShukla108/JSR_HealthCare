from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet

from core.serializers import RegisterSerializer, LoginSerializer

from core.models import User    
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# # Create your views here.

class RegisterViewset(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = RegisterSerializer
    # permission_classes = [All]
    def get_queryset(self):
        return User.objects.all()
    
    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        print(f'user : {user}')
        return Response({
            'User' : serializer.data,
            'Access Token': str(access_token)
        }, status=status.HTTP_201_CREATED)


class LoginViewset(ViewSet):

    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refreshToken = RefreshToken.for_user(user=user)
        accessToken = refreshToken.access_token

        return Response(
            {
                "user" : {
                    "refresh_token" : str(refreshToken),
                    "access_token" : str(accessToken),
                    "role" : user.role
                }
            },
            status=status.HTTP_200_OK
        )