from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# from core.utils import ROLES

# ROLES = ( ("PATIENT", "patient"), ("DOCTOR", "doctor"), ("NURSE", "nurse"), ("ADMIN", "admin"), ("RECEPTIONIST", "receptionist"), ("ADMIN", "admin") )

class User(AbstractUser):

    class User_Roles(models.TextChoices):
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        ADMIN = "ADMIN", "Admin"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"


    Full_name = models.CharField(max_length=50, null=False)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # username = models.CharField(max_length=50, unique=True, editable=False)    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(null=True, max_length=15)
    role = models.CharField(choices=User_Roles.choices, default="PATIENT", max_length=50)
    is_verified = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.username:
            self.username = f'user_{self.role}_{uuid4()}'

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email} | ROLE : {self.role}'