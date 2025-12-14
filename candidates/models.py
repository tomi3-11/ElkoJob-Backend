from django.db import models
from django.contrib.auth.models import User

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True) 
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    work_type = models.CharField(max_length=50, blank=True)  # Remote, Hybrid, etc.
    subscription_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50)  # Full time, contract
    level = models.CharField(max_length=50)  # Internship, senior
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)  # Remote, Hybrid
    salary_range = models.CharField(max_length=50)  # e.g., 0-100k
    category = models.CharField(max_length=100)  # Engineering, etc.
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.user.username} -> {self.job.title}"
