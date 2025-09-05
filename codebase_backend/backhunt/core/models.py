from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


# Create your models here.
# ROLES = {
#     "DOCTOR": {
#         "General Practitioner": [],
#         "Consultant": [
#             "Cardiologist",
#             "Neurologist",
#             "Orthopedic Surgeon",
#             "Dermatologist",
#             "Oncologist",
#             "Pediatrician",
#             "Endocrinologist",
#             "Psychiatrist",
#         ],
#         "Specialty Doctor": [
#             "Emergency Medicine",
#             "Radiology",
#             "Anesthesiology",
#             "Pathology"
#         ],
#         "Foundation Doctor": [
#             "Foundation Year 1 (Intern)",
#             "Foundation Year 2 (Resident)"
#         ],
#         "Registrar / Specialty Trainee": [],
#         "Locum Doctor": [],
#         "Public Health Doctor": [],
#         "Academic / Research Doctor": []
#     },

#     "NURSE": {
#         "Registered Nurse": [
#             "Adult Nurse",
#             "Children’s Nurse (Pediatric)",
#             "Learning Disability Nurse",
#             "Mental Health Nurse"
#         ],
#         "Advanced Nurse Practitioner": [],
#         "Nurse Consultant": [],
#         "Clinical Nurse Specialist": [],
#         "Practice Nurse": [],
#         "Community / District Nurse": [],
#         "Midwife": [],
#         "Health Visitor": []
#     },

#     "ADMIN": {
#         "Medical Secretary / PA": [],
#         "Medical Records Clerk": [],
#         "Billing Specialist": [],
#         "HR Officer": [],
#         "Healthcare IT Administrator": [],
#         "Practice Manager": [],
#         "Data Entry Clerk": [],
#         "Finance / Admin Officer": [],
#         "Compliance & Governance Officer": []
#     },

#     "RECEPTIONIST": {
#         "Front Desk Receptionist": [],
#         "Patient Services Coordinator": [],
#         "Call Handler / Telephonist": [],
#         "Scheduling Coordinator": [],
#         "Outpatient Receptionist": [],
#         "Ward Clerk": [],
#         "Registration Officer": []
#     }
# }

# ROLES = ( ("PATIENT", "patient"), ("DOCTOR", "doctor"), ("NURSE", "nurse"), ("ADMIN", "admin"), ("RECEPTIONIST", "receptionist"), ("ADMIN", "admin") )

class User(AbstractUser):

    class Roles(models.TextChoices):
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        ADMIN = "ADMIN", "Admin"
        RECEPTIONIST = "RECEPTIONIST", "Receptionist"

    Full_name = models.CharField(max_length=50, null=False)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, editable=False)    
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(null=True)
    role = models.CharField(choices=Roles.choices, default="PATIENT", max_length=50)
    password = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.username:
            self.username = f'user_{self.role}_{self.email}'

        super().save(*args, **kwargs)

    def __self__(self):
        return f'{self.email} | ROLE : {self.role}'