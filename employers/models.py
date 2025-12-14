from django.db import models
from django.contrib.auth.models import User
from candidates.models import CandidateProfile

class JobMatchRequest(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")  # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)
