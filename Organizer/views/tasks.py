from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic as generic_views

from Overhead import util
from Organizer import models as organizer_models
from Organizer import forms as organizer_forms

class TaskList(util.ForcedAuthenticationMixin, generic_views.TemplateView):
    template_name = 'organizer/tasks/list.html'

    def get_context_data(self, **kwargs):
        # request should not be None, TemplateViewSimple ensures this
        context = super(TaskList, self).get_context_data(**kwargs)

        clients = organizer_models.Client.objects.filter(Q(user=self.request.user) | Q(limited=False))
        projects = organizer_models.Project.objects.filter(client__in=clients)
        tasks = organizer_models.Task.objects.filter(project__in=projects)

        context['clients'] = clients.all()
        context['projects'] = projects.all()
        context['tasks'] = tasks.all()

        return context

class TaskEditMixin:
    template_name = 'organizer/generic_forms/edit_form.html'
    form_class = organizer_forms.TaskForm
    model = organizer_models.Task
    success_url = reverse_lazy('tasks.list')
class TaskEdit(TaskEditMixin, UpdateView):
    pass
class TaskCreate(TaskEditMixin, CreateView):
    pass
class TaskDelete(TaskEditMixin, DeleteView):
    template_name = 'organizer/tasks/delete_form.html'
