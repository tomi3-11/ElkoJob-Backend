from django.urls import path
from .views import (
    JobCreateView, MyJobsListView, EmployerDashboardView,
    CandidateListView, CandidateDetailView, JobMatchRequestView,
    CandidateResumeDownloadView
)

urlpatterns = [
    path("jobs/", JobCreateView.as_view(), name="job-create"),
    path("jobs/my/", MyJobsListView.as_view(), name="my-jobs"),
    path("dashboard/", EmployerDashboardView.as_view(), name="dashboard"),
    path("candidates/", CandidateListView.as_view(), name="candidates"),
    path("candidates/<int:id>/", CandidateDetailView.as_view(), name="candidate-detail"),
    path("candidates/<int:id>/match/", JobMatchRequestView.as_view(), name="candidate-match"),
    path("candidates/<int:id>/resume/", CandidateResumeDownloadView.as_view(), name="candidate-resume"),
]
