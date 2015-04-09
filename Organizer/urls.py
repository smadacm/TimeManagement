from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from Organizer import views as organizer_views

urlpatterns = patterns('Organizer.views',
                       url(r'^clients/list/$', organizer_views.ClientList.as_view(), name='clients.list'),
                       url(r'^clients/edit/?$', organizer_views.ClientCreate.as_view(), name='clients.create'),
                       url(r'^clients/edit/(?P<pk>\d*)/?$', organizer_views.ClientEdit.as_view(), name='clients.edit'),
                       url(r'^clients/delete/(?P<pk>\d*)/?$', organizer_views.ClientDelete.as_view(), name='clients.delete'),

                       url(r'^projects/list/$', organizer_views.ProjectList.as_view(), name='projects.list'),
                       url(r'^projects/edit/?$', organizer_views.ProjectCreate.as_view(), name='projects.create'),
                       url(r'^projects/edit/(?P<pk>\d*)/?$', organizer_views.ProjectEdit.as_view(), name='projects.edit'),
                       url(r'^projects/delete/(?P<pk>\d*)/?$', organizer_views.ProjectDelete.as_view(), name='projects.delete'),

                       url(r'^tasks/list/$', organizer_views.TaskList.as_view(), name='tasks.list'),
                       url(r'^tasks/edit/?$', organizer_views.TaskCreate.as_view(), name='tasks.create'),
                       url(r'^tasks/edit/(?P<pk>\d*)/?$', organizer_views.TaskEdit.as_view(), name='tasks.edit'),
                       url(r'^tasks/delete/(?P<pk>\d*)/?$', organizer_views.TaskDelete.as_view(), name='tasks.delete'),

                       url(r'^dashboard/$', organizer_views.Dashboard.as_view(), name='dashboard'),
                       url(r'^dashboard/tasks/delete/(?P<pk>\d+)$', organizer_views.DashboardDeleteTaskView.as_view(), name='dashboard.tasks.delete'),

                       url(r'^async/clients/get$', organizer_views.DashboardAsyncGetClients.as_view(), name='async.clients.get'),
                       url(r'^async/projects/get/(?P<client>\d+)$', organizer_views.DashboardAsyncGetProjects.as_view(), name='async.projects.get'),
                       # url(r'^async/tasks/get$', organizer_views.DashboardAsyncGetClients.as_view(), name='async.tasks.get'),
                       url(r'^async/tasks/put$', csrf_exempt(organizer_views.DashboardAsyncPutTask.as_view()), name='async.tasks.put'),
)
