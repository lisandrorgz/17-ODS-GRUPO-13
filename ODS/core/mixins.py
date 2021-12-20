from django.core.exceptions          import PermissionDenied

class AdminRequiredMixins():
    # VER CONDICIONES DE permisos_requeridos = []
        def dispatch(self, request, *args, **kwars):
        # print(self.permisos_requeridos)
            if not request.user.is_superuser:
                raise PermissionDenied
            return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)