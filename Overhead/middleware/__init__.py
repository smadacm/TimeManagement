from django import shortcuts
from Overhead import util

class UnAuthorized(object):
    def process_exception(self, request, e):
        if type(e) == util.HTTP401Exception:
            # redirect
            return shortcuts.redirect('overhead.login')
        return