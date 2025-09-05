from rest_framework.serializers import ModelSerializer
from core.models import User    

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'Full_name', 'username', 'email', 'phone_number', 'role', 'is_verified', 'created', 'updated']

        read_only_fields = ['id', 'is_superuser', 'updated', 'created']