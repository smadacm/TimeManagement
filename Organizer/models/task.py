from django.db import models
from django.contrib.auth.models import User

import project

class TaskSeverity(models.Model):
    name = models.CharField('Name', max_length=255)
    sort_order = models.IntegerField('Sort Order', default=99)

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.TextField('Title')
    notes = models.TextField('Notes', default='', blank=True)
    project = models.ForeignKey(project.Project)
    severity = models.ForeignKey('TaskSeverity')
    due = models.DateField('Due Date', blank=True, null=True, default=None)
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
        return project.Project.objects.filter(name='Default').first()

    def set_defaults(self):
        self.severity = self.default_severity
        self.project = self.default_project
