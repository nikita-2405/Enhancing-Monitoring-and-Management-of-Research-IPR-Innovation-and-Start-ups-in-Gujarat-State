
from rest_framework.permissions import BasePermission


# Common permission helper
def is_admin(request):
    return request.user.is_authenticated and request.user.is_superuser


# Individual Role Permissions

class IsResearcher(BasePermission):
    def has_permission(self, request, view):
        return (
            is_admin(request)
            or (
                request.user.is_authenticated
                and request.user.groups.filter(name='Researcher').exists()
            )
        )


class IsInnovator(BasePermission):
    def has_permission(self, request, view):
        return (
            is_admin(request)
            or (
                request.user.is_authenticated
                and request.user.groups.filter(name='Innovator').exists()
            )
        )


class IsEntrepreneur(BasePermission):
    def has_permission(self, request, view):
        return (
            is_admin(request)
            or (
                request.user.is_authenticated
                and request.user.groups.filter(name='Entrepreneur').exists()
            )
        )


class IsIPRProfessional(BasePermission):
    def has_permission(self, request, view):
        return (
            is_admin(request)
            or (
                request.user.is_authenticated
                and request.user.groups.filter(name='IPR Professional').exists()
            )
        )


class IsPolicymaker(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name='Policymaker').exists()
            and request.method in ['GET', 'HEAD', 'OPTIONS']
        )


# Role + Policymaker Read-Only Permissions

class IsResearcherOrPolicymaker(BasePermission):
    def has_permission(self, request, view):
        if is_admin(request):
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='Researcher').exists():
            return True

        return (
            request.user.groups.filter(name='Policymaker').exists()
            and request.method in ['GET', 'HEAD', 'OPTIONS']
        )


class IsInnovatorOrPolicymaker(BasePermission):
    def has_permission(self, request, view):
        if is_admin(request):
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='Innovator').exists():
            return True

        return (
            request.user.groups.filter(name='Policymaker').exists()
            and request.method in ['GET', 'HEAD', 'OPTIONS']
        )


class IsIPRProfessionalOrPolicymaker(BasePermission):
    def has_permission(self, request, view):
        if is_admin(request):
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='IPR Professional').exists():
            return True

        return (
            request.user.groups.filter(name='Policymaker').exists()
            and request.method in ['GET', 'HEAD', 'OPTIONS']
        )


class IsEntrepreneurOrPolicymaker(BasePermission):
    def has_permission(self, request, view):
        if is_admin(request):
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='Entrepreneur').exists():
            return True

        return (
            request.user.groups.filter(name='Policymaker').exists()
            and request.method in ['GET', 'HEAD', 'OPTIONS']
        )
