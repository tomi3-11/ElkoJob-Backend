from django.db import models
from django.contrib.auth.models import User

class CandidateProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="candidate_profile"
    )
    bio = models.TextField(blank=True)
    skills = models.JSONField(default=list, blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    subscription_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} profile"


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

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    salary_range = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    candidate = models.ForeignKey(
        CandidateProfile,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("candidate", "job")

    def __str__(self):
        return f"{self.candidate.user.username} → {self.job.title}"
