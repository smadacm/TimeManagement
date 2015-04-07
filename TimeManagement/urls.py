from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='dashboard', permanent=False), name='home'),
    url(r'^organizer/', include('Organizer.urls')),
    url(r'^overhead/', include('Overhead.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
