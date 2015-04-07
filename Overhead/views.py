import django.contrib.auth as auth
import django.shortcuts as shortcuts
from django.conf import settings

# Create your views here.

def login_page(request, error=None, info=None):
    context = {
        'error':error,
        'info':info,
        'redirect':request.GET.get('redirect'),
    }
    return shortcuts.render(request, 'login.html', context)
def login_action(request):
    post = request.POST
    un = post['username']
    pw = post['password']

    user = auth.authenticate(username=un, password=pw)
    if user is None:
        return shortcuts.redirect('overhead.login')

    auth.login(request, user)

    redir = settings.OVERHEAD_AFTER_LOGIN_ACTION
    if post.has_key('redirect'):
        redir = '/' + post['redirect'].lstrip('/')
    return shortcuts.redirect(redir)

def logout_action(request):
    auth.logout(request)

    post = request.POST

    redir = '/'
    if post.has_key('redirect'):
        redir = '/' + post['redirect'].lstrip('/')
    return shortcuts.redirect(redir)

def register_page(request):
    pass
def register_action(request):
    pass
def forgot_password_page(request):
    pass
def forgot_password_action(request):
    pass
