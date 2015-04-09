import datetime

from django.template.loader import get_template
from django.template import RequestContext

import client
import task


class DashboardPanelAbstract(object):
    template_dir = 'organizer/dashboard/panels'
    template_filename = 'generic.html'
    title = 'Tasks'
    panel_type = 'primary'

    def __init__(self, request, **kwargs):
        self.request = request
        self.params = kwargs

    @property
    def template_name(self):
        return '/'.join((self.template_dir, self.template_filename))

    def get_base_data(self):
        data = self.params
        data['title'] = self.title
        data['panel_type'] = self.panel_type
        return data

    @property
    def data(self):
        return self.params

    def render(self):
        template = get_template(self.template_name)
        return template.render(RequestContext(self.request, self.data))

class UnclassifiedPanelAbstract(DashboardPanelAbstract):
    template_filename = 'unclassified_tasks.html'

class CreateTaskPanel(DashboardPanelAbstract):
    template_filename = 'create_task.html'

class AllTasksPanel(DashboardPanelAbstract):
    template_filename = 'classified_tasks.html'

    @property
    def data(self):
        data = self.get_base_data()
        if 'clients' not in data:
            clients = client.Client.get_by_request(self.request)
            data['clients'] = clients
        return data

class TimeBasedPanel(UnclassifiedPanelAbstract):
    display_if_empty = True
    empty_display_text = 'Nothing fits this description'

    def get_time_filters(self):
        return {}

    def get_base_data(self):
        data = super(TimeBasedPanel, self).get_base_data()
        data['display_if_empty'] = self.display_if_empty
        data['empty_display_text'] = self.empty_display_text
        return data

    @property
    def data(self):
        data = self.get_base_data()
        filters = self.get_time_filters()
        filters['user'] = self.request.user

        data['tasks'] = task.Task.objects.filter(**filters).all()
        return data

class PastDuePanel(TimeBasedPanel):
    title = 'Past Due'
    panel_type = 'danger'
    display_if_empty = False

    def get_time_filters(self):
        filters = {
            'due__lte': datetime.date.today(),
            }
        return filters

class DueTodayPanel(TimeBasedPanel):
    title = 'Due Today'
    empty_display_text = 'Nothing due today'

    def get_time_filters(self):
        filters = {
            'due': datetime.date.today(),
            }
        return filters

class DueThisWeekPanel(TimeBasedPanel):
    title = 'Due This Week'
    empty_display_text = 'Nothing due this week'

    def get_time_filters(self):
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())
        week_end = week_start + datetime.timedelta(days=6)

        filters = {
            'due__lte': week_end,
            'due__gte': week_start,
            }
        return filters
