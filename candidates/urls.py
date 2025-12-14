# accounts/urls.py
from django.urls import path
from .views import CandidateProfileView, JobListView, JobApplyView

urlpatterns = [
    path("candidates/profile/", CandidateProfileView.as_view(), name="candidate_profile"),
    path("candidates/jobs/", JobListView.as_view(), name="job_list"),
    path("candidates/jobs/<int:pk>/apply/", JobApplyView.as_view(), name="job_apply"),
]
