from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # Maps HTTP methods to required model permissions
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
      if not request.user or not request.user.is_authenticated:
          print("Denied: unauthenticated user")
          return False
      if not request.user.is_staff:
          print("Denied: not staff")
          return False
      return super().has_permission(request, view)


    # Optional object-level control
    # def has_object_permission(self, request, view, obj):
    #     return request.user == obj.owner
