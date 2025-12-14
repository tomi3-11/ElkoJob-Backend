from django.db import models
from django.contrib.auth.models import User
from candidates.models import CandidateProfile

class JobMatchRequest(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")  # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("full_time", "Full Time"),
        ("contract", "Contract"),
    ]

    LEVEL_CHOICES = [
        ("intern", "Internship"),
        ("senior", "Senior"),
    ]

    WORK_TYPE_CHOICES = [
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
        ("onsite", "Onsite"),
    ]

    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    salary_range = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
