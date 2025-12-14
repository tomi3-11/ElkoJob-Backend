from rest_framework import serializers
from .models import JobMatchRequest, Job
from candidates.models import CandidateProfile

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class JobMatchRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobMatchRequest
        fields = "__all__"

class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ["id", "user", "skills", "bio", "experience", "location", "resume"]
