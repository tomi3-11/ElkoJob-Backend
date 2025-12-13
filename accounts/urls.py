from django.urls import path, include

urlpatterns = [
    # DRF ViewSet routes
    path('auth/', include('dj_rest_auth.urls')),  # login, logout, password
    path('auth/registration/', include('dj_rest_auth.registration.urls')), 
]
