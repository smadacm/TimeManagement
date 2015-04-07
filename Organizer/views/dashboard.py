from django.db.models import Q
from django.http import JsonResponse
from django.template import RequestContext
from django.views import generic as generic_views

from Organizer import models as organizer_models

from Overhead import util

class Dashboard(util.ForcedAuthenticationMixin, generic_views.TemplateView):
    template_name = 'organizer/dashboard.html'

    def get_context_data(self, **kwargs):
        # request should not be None, TemplateViewSimple ensures this
        context = super(Dashboard, self).get_context_data(**kwargs)

        clients = organizer_models.Client.get_by_request(self.request)
        dashboard = organizer_models.Dashboard.get_by_request(self.request)

        context['clients'] = clients
        context['dashboard'] = dashboard

        return context
dashboard = Dashboard.as_view()

# based on code from the Django doc site (https://docs.djangoproject.com/en/1.8/topics/class-based-views/mixins/)
class JSONResponseView(generic_views.View):
    def do_return(self, payload):
        ret = {'payload': payload, 'size': len(payload)}
        return JsonResponse(ret)

    def get(self, request, *args, **kwargs):
        data = self.get_payload(**kwargs)
        return self.do_return(data)

    def get_payload(self,**kwargs):
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return kwargs

class DashboardAsyncGetClients(util.ForcedAuthenticationMixin, JSONResponseView):
    def get_payload(self, **kwargs):
        clients = organizer_models.Client.objects.filter(Q(user=self.request.user) | Q(limited=False))
        clients_d = dict([(client.name, client.id) for client in clients])
        return clients_d

class DashboardAsyncGetProjects(util.ForcedAuthenticationMixin, JSONResponseView):
    def get_payload(self, **kwargs):
        clients = organizer_models.Project.objects.filter(client__pk=kwargs['client'])
        clients_d = dict([(client.name, client.id) for client in clients])
        return clients_d

class DashboardAsyncPutTask(util.ForcedAuthenticationMixin, JSONResponseView):
    def post(self, request, *args, **kwargs):
        fail_messages = []

        task = organizer_models.Task()
        task.set_defaults()
        post = request.POST
        user = request.user

        if 'client' in post and len(post['client']):
            task.client_id = int(post['client'])
        else:
            fail_messages.append('No client selected')

        if 'project' in post and len(post['project']):
            task.project_id = int(post['project'])
        else:
            fail_messages.append('No project selected')

        if 'title' in post and len(post['title']):
            task.title = post['title']
        else:
            fail_messages.append('No title given')

        if 'due' in post and len(post['due']):
            task.due = post['due']

        if not fail_messages:
            task.user = user
            task.save()
            data = 'success'
        else:
            data = fail_messages
        return self.do_return(data)

    def get_payload(self, **kwargs):
        print kwargs
        clients = organizer_models.Project.objects.filter(client__pk=kwargs['client'])
        clients_d = dict([(client.name, client.id) for client in clients])
        return clients_d
