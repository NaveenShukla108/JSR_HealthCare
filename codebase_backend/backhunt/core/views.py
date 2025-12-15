from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

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


class LoginViewset(ModelViewSet):

    http_method_names = ['post']
    serializer_class = LoginSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(user=user)
