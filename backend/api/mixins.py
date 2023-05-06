from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StafferEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]