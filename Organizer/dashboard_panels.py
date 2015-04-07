from django.template.loader import get_template
from django.template import RequestContext
from . import models as organizer_models

class DashboardPanelAbstract(object):
    template_dir = 'organizer/dashboard/panels'
    template_filename = 'generic.html'

    def __init__(self, request, **kwargs):
        self.request = request
        self.params = kwargs

    @property
    def template(self):
        return '/'.join((self.template_dir, self.template_filename))

    @property
    def data(self):
        return self.params

    def render(self):
        template = get_template(self.template_name)
        return template.render(RequestContext(self.request, self.data))

class CreateTaskPanel(DashboardPanelAbstract):
    template_filename = 'create_task.html'

class AllTasksPanel(DashboardPanelAbstract):
    template_filename = 'classified_tasks.html'

    @property
    def data(self):
        data = self.params
        if 'clients' not in data:
            clients = organizer_models.Client.get_by_request(self.request)
            data['clients'] = clients
        return data

class DueTodayPanel(DashboardPanelAbstract):
    template_filename = 'unclassified_tasks.html'

class DueThisWeekPanel(DashboardPanelAbstract):
    template_filename = 'unclassified_tasks.html'
