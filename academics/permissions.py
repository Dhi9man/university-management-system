from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsFacultyOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_authenticated and
                request.user.groups.filter(name__in=["Faculty", "Admin"]).exists())


class IsStudentSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Students can see only their own records via API
        if request.user.groups.filter(name="Student").exists():
            return hasattr(obj, "user") and obj.user == request.user
        return True
