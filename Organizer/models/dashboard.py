from django.db import models
from django.contrib.auth.models import User

import panels


class Dashboard(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):
        un = ''
        if self.user is None:
            un = 'Other Users'
        else:
            un = self.user.username
        return 'Dashboard for %s'%(un,)
    def __unicode__(self):
        return unicode(str(self))

    @classmethod
    def get_or_create_by_request(cls, request):
        user = request.user
        dashboard = cls.objects.filter(user=user)
        if len(dashboard) == 0:
            dashboard = cls()
            dashboard.user = user
            dashboard.save()
        else:
            dashboard = dashboard.first()

        return dashboard

    @classmethod
    def get_by_request(cls, request, **params):
        user = request.user
        dashboard = cls.objects.filter(user=user)
        if len(dashboard) == 0:
            dashboard = cls.objects.filter(user=None)
        dashboard = dashboard.first()
        dashboard.set_request(request)
        dashboard.prep_panels(request, **params)
        return dashboard

    def set_request(self, request):
        self.request = request

    def prep_panels(self, request=None, **params):
        self.panels = self.dashboardpanel_set.all()
        if request is None: request = self.request
        for p in self.panels:
            p.init(request, **params)

    def render_panels(self):
        results = []
        for panel in self.panels:
            results.append(panel.render())
        return '\n'.join(results)

class DashboardPanel(models.Model):
    PANEL_TYPES = (
        ('CreateTaskPanel', 'Create Task'),
        ('AllTasksPanel', 'All Tasks'),
        ('DueTodayPanel', 'Due Today'),
        ('DueThisWeekPanel', 'Due This Week'),
        ('PastDuePanel', 'Past Due'),
    )
    panel_types_d = dict(PANEL_TYPES)
    dashboard = models.ForeignKey(Dashboard)
    type = models.CharField('Panel Type', choices=PANEL_TYPES, max_length=100)
    sort_order = models.IntegerField('Sort Order', default=99)

    class Meta:
        ordering = ['sort_order',]

    def __str__(self):
        return '"%s" Panel of %s'%(self.panel_types_d.get(self.type, 'Unknown'), self.dashboard,)
    def __unicode__(self):
        return unicode(str(self))

    def init(self, request, **params):
        self.request = request
        self.params = params

    @property
    def panel(self):
        return getattr(panels, self.type)(self.request, **self.params)

    def render(self):
        return self.panel.render()

