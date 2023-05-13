from rest_framework.permissions import BasePermission

from config.constants.RoleChoices import ROLES


class StudentPermission(BasePermission):
    message = "student"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name == ROLES.STUDENT


class TeacherPermission(BasePermission):
    message = "teacher"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and \
            (request.user.role.name == ROLES.TEACHER or request.user.role.name == ROLES.SUPER_ADMIN)


class AdminPermission(BasePermission):
    message = "admin"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == ROLES.SUPER_ADMIN
