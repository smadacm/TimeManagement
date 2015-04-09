from django.db import models
from django.contrib.auth.models import User

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
