from rest_framework import permissions

from .models import *


class CanCreateApplication(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.userrole in [User.UserRoles.Admin, User.UserRoles.Judges]

class CanUpdateApplication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.userrole in [User.UserRoles.Admin, User.UserRoles.Staff, User.UserRoles.EscaleStaff]

class CanReadApplication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.userrole in [User.UserRoles.Admin, User.UserRoles.Staff, User.UserRoles.EscaleStaff, User.UserRoles.Users]
