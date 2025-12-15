ROLES = {
    "DOCTOR": {
        "General Practitioner": [],
        "Consultant": [
            "Cardiologist",
            "Neurologist",
            "Orthopedic Surgeon",
            "Dermatologist",
            "Oncologist",
            "Pediatrician",
            "Endocrinologist",
            "Psychiatrist",
        ],
        "Specialty Doctor": [
            "Emergency Medicine",
            "Radiology",
            "Anesthesiology",
            "Pathology"
        ],
        "Foundation Doctor": [
            "Foundation Year 1 (Intern)",
            "Foundation Year 2 (Resident)"
        ],
        "Registrar / Specialty Trainee": [],
        "Locum Doctor": [],
        "Public Health Doctor": [],
        "Academic / Research Doctor": []
    },

    "NURSE": {
        "Registered Nurse": [
            "Adult Nurse",
            "Children’s Nurse (Pediatric)",
            "Learning Disability Nurse",
            "Mental Health Nurse"
        ],
        "Advanced Nurse Practitioner": [],
        "Nurse Consultant": [],
        "Clinical Nurse Specialist": [],
        "Practice Nurse": [],
        "Community / District Nurse": [],
        "Midwife": [],
        "Health Visitor": []
    },

    "ADMIN": {
        "Medical Secretary / PA": [],
        "Medical Records Clerk": [],
        "Billing Specialist": [],
        "HR Officer": [],
        "Healthcare IT Administrator": [],
        "Practice Manager": [],
        "Data Entry Clerk": [],
        "Finance / Admin Officer": [],
        "Compliance & Governance Officer": []
    },

    "RECEPTIONIST": {
        "Front Desk Receptionist": [],
        "Patient Services Coordinator": [],
        "Call Handler / Telephonist": [],
        "Scheduling Coordinator": [],
        "Outpatient Receptionist": [],
        "Ward Clerk": [],
        "Registration Officer": []
    }
}


ROLE_CHOICES = [
    ("DOCTOR", "Doctor"),
    ("NURSE", "Nurse"),
    ("ADMIN", "Admin"),
    ("RECEPTIONIST", "Receptionist"),
    ("PATIENT", "Patient")
]