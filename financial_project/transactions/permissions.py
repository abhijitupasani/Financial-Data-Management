from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsFinancialAnalystOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Placeholder for a real role check; assume all authenticated users for now
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class IsAuditorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Auditor role check could be added here
            return request.user and request.user.is_authenticated
        return False
