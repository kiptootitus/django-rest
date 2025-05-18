from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        user = self.request.user
        lookup_data[self.user_field] = user
        print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)
        print(qs)
        if user.is_staff:
            return qs
        return qs.filter(**lookup_data)
