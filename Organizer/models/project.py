import client
from django.db import models
from django.contrib.auth.models import User

class ProjectPriority(models.Model):
    name = models.CharField('Name', max_length=255)
    sort_order = models.IntegerField('Sort Order', default=99)

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField('Name', max_length=255)
    client = models.ForeignKey(client.Client)
    priority = models.ForeignKey(ProjectPriority)
    user = models.ManyToManyField(User)
    filtered_tasks = []

    def __unicode__(self):
        return str(self)
    def __str__(self):
        return self.name

    def load_tasks_by_request(self, request):
        self.filtered_tasks = self.task_set.filter(user=request.user)
