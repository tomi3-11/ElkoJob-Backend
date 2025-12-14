from rest_framework import permissions

class isEmployer(permissions.BasePermission):
    """
    Allow access only to users marked as employers.
    """
    
    def has_permission(self, request):
        return bool(request.user and request.user.is_authenticated and request.user.is_employer)
    