from django.conf.urls import patterns, include, url

urlpatterns = patterns('Overhead.views',
    url(r'^login/$', 'login_page', name='overhead.login'),
    url(r'^login/action/$', 'login_action', name='overhead.login_action'),
    url(r'^logout/$', 'logout_action', name='overhead.logout'),
)
