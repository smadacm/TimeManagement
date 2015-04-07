from django.db import models
from django.contrib.auth.models import User

from Organizer import dashboard_panels

# Create your models here.

class ProjectPriority(models.Model):
    name = models.CharField('Name', max_length=255)
    sort_order = models.IntegerField('Sort Order', default=99)

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

class TaskSeverity(models.Model):
    name = models.CharField('Name', max_length=255)
    sort_order = models.IntegerField('Sort Order', default=99)

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField('Name', max_length=255)
    abbreviation = models.CharField('Abbreviation', max_length=10, unique=True)
    user = models.ManyToManyField(User)
    limited = models.BooleanField('User-Restricted', default=False)
    filtered_projects = []

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

    @classmethod
    def get_default(cls):
        possibles = cls.objects.filter(abbreviation='default')
        if not possibles:
            ret = Client(name='Other', abbreviation='default', limited=False)
            ret.save()
        else:
            ret = possibles.first()
        return ret

    def load_projects(self, request, load_tasks=True):
        self.filtered_projects = self.project_set.all()
        if load_tasks:
            for p in self.filtered_projects:
                p.load_tasks_by_request(request)

    @classmethod
    def get_by_request(cls, request, load_projects=True, load_tasks=True):
        clients = cls.objects.filter(models.Q(user=request.user) | models.Q(limited=False))
        clients = clients.all()

        if load_projects:
            for c in clients:
                c.load_projects(request, load_tasks=load_tasks)

        return clients

class ClientNotes(models.Model):
    user = models.ForeignKey(User)
    client = models.ForeignKey(Client)
    note = models.TextField('Note')

class Project(models.Model):
    name = models.CharField('Name', max_length=255)
    client = models.ForeignKey(Client)
    priority = models.ForeignKey(ProjectPriority)
    user = models.ManyToManyField(User)
    filtered_tasks = []

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

    def load_tasks_by_request(self, request):
        self.filtered_tasks = self.task_set.filter(user=request.user)

class Task(models.Model):
    title = models.TextField('Title')
    notes = models.TextField('Notes', default='', blank=True)
    project = models.ForeignKey(Project)
    severity = models.ForeignKey('TaskSeverity')
    due = models.DateTimeField('Due Date', blank=True, null=True, default=None)
    user = models.ForeignKey(User)
    active = models.BooleanField('Active', default=True)

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.title

    @property
    def default_severity(self):
        return TaskSeverity.objects.filter(name='Standard').first()
    @property
    def default_project(self):
        return Project.objects.filter(name='Default').first()

    def set_defaults(self):
        self.severity = self.default_severity
        self.project = self.default_project

class Dashboard(models.Model):
    user = models.ForeignKey(User, blank=True, unique=True)

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
    def get_by_request(cls, request):
        user = request.user
        dashboard = cls.objects.filter(user=user)
        if len(dashboard) == 0:
            dashboard = cls.objects.filter(user='')
        dashboard = dashboard.first()
        dashboard.set_request(request)
        return dashboard

    def set_request(self, request):
        self.request = request

    def render_panels(self):
        results = []
        for panel in self.dashboardpanel_set.all():
            results.append(panel.render())
        return '\n'.join(results)

class DashboardPanel(models.Model):
    PANEL_TYPES = (
        ('CreateTaskPanel', 'Create Task'),
        ('AllTasksPanel', 'All Tasks'),
        ('DueTodayPanel', 'Due Today'),
        ('DueThisWeekPanel', 'Due This Week'),
    )
    dashboard = models.ForeignKey(Dashboard)
    type = models.CharField('Panel Type', choices=PANEL_TYPES)
    sort_order = models.IntegerField('Sort Order', default=99)

    def init(self, request, **params):
        self.request = request
        self.params = params

    @property
    def panel(self):
        if not hasattr(self, 'panel'):
            self.panel = getattr(dashboard_panels, self.type)(self.request, **self.params)
        return self.panel

    def render(self):
        return self.panel.render()
