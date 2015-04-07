from django import shortcuts
from django.views import generic as generic_views

class HTTP401Exception(Exception):
    pass

class ForcedAuthenticationMixin(object):
    def check_user(self):
        if not self.request.user.is_authenticated():
            raise HTTP401Exception("Unauthorized")
        return

    def dispatch(self, request, *args, **kwargs):
        self.check_user()
        return super(ForcedAuthenticationMixin, self).dispatch(request, *args, **kwargs)
