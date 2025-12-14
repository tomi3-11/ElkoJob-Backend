from rest_framework import serializers
from .models import JobMatchRequest
from candidates.models import CandidateProfile, Job

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
