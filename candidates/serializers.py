from rest_framework import serializers
from .models import CandidateProfile, Job, JobApplication

class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ["bio", "skills", "resume", "subscription_active"]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ["id", "job", "applied_at"]
        read_only_fields = ["applied_at"]

    def validate(self, attrs):
        request = self.context["request"]
        job = self.context["job"]
        candidate = request.user.candidate_profile

        if JobApplication.objects.filter(candidate=candidate, job=job).exists():
            raise serializers.ValidationError("You already applied for this job")

        return attrs
