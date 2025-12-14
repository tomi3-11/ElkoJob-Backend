from rest_framework import generics, permissions, filters, serializers
from .models import CandidateProfile, Job, JobApplication
from .serializers import CandidateProfileSerializer, JobSerializer, JobApplicationSerializer

class CandidateProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.candidate_profile


class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Job.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["type", "level", "country", "city", "work_type", "salary_range", "category"]


class JobApplyView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        candidate_profile = self.request.user.candidate_profile

        if not candidate_profile.subscription_active:
            raise serializers.ValidationError("Active subscription required to apply")

        job = Job.objects.get(pk=self.kwargs["pk"])
        serializer.context["job"] = job
        serializer.save(candidate=candidate_profile, job=job)
