from rest_framework import generics, permissions, filters
from .models import JobMatchRequest, Job
from .serializers import JobSerializer, JobMatchRequestSerializer, CandidateProfileSerializer
from candidates.models import CandidateProfile
from employers.permissions import IsEmployer
from rest_framework.response import Response


# Post a new job
class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

# List active job listings for employer
class MyJobsListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user, is_active=True)

# Employer dashboard metrics
class EmployerDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.filter(employer=request.user)
        total_jobs = jobs.count()
        total_views = sum(getattr(job, "views", 0) for job in jobs)  # Assuming a views field
        total_applicants = sum(job.jobapplication_set.count() for job in jobs)
        return Response({
            "total_jobs": total_jobs,
            "total_views": total_views,
            "total_applicants": total_applicants
        })

# Browse/Search candidates
class CandidateListView(generics.ListAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]
    queryset = CandidateProfile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["skills", "experience", "location"]

# View specific candidate
class CandidateDetailView(generics.RetrieveAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]
    queryset = CandidateProfile.objects.all()
    lookup_field = "id"

# Request matching
class JobMatchRequestView(generics.CreateAPIView):
    serializer_class = JobMatchRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        candidate_id = self.kwargs.get("id")
        candidate = CandidateProfile.objects.get(id=candidate_id)
        serializer.save(employer=self.request.user, candidate=candidate)

# Download resume
from django.http import FileResponse

class CandidateResumeDownloadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get(self, request, *args, **kwargs):
        candidate_id = self.kwargs.get("id")
        candidate = CandidateProfile.objects.get(id=candidate_id)
        return FileResponse(candidate.resume.open(), as_attachment=True, filename=f"{candidate.user.username}_resume.pdf")
