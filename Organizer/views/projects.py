from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic as generic_views

from Overhead import util
from Organizer import models as organizer_models
from Organizer import forms as organizer_forms

class ProjectList(util.ForcedAuthenticationMixin, generic_views.TemplateView):
    template_name = 'organizer/projects/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)

        clients = organizer_models.Client.objects.filter(Q(user=self.request.user) | Q(limited=False))
        projects = organizer_models.Project.objects.filter(client__in=clients)
        context['clients'] = clients.all()
        context['projects'] = projects.all()

        return context

class ProjectEditMixin:
    template_name = 'organizer/generic_forms/edit_form.html'
    form_class = organizer_forms.ProjectForm
    model = organizer_models.Project
    success_url = reverse_lazy('projects.list')
class ProjectEdit(util.ForcedAuthenticationMixin, ProjectEditMixin, UpdateView):
    pass
class ProjectCreate(util.ForcedAuthenticationMixin, ProjectEditMixin, CreateView):
    pass
class ProjectDelete(util.ForcedAuthenticationMixin, ProjectEditMixin, DeleteView):
    template_name = 'organizer/projects/delete_form.html'
