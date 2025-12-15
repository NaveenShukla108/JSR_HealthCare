from rest_framework import serializers
from core.models import User    

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'Full_name', 'email', 'phone_number', 'role', 'password', 'is_verified', 'created', 'updated']

        read_only_fields = ['id', 'is_superuser', 'updated', 'created', 'username']

    
    def create(self, validated_data):
        poped_password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(poped_password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['email', 'password']

    
