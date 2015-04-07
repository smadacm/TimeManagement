from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic as generic_views

from Overhead import util
from Organizer import models as organizer_models
from Organizer import forms as organizer_forms

class ClientList(util.ForcedAuthenticationMixin, generic_views.TemplateView):
    template_name = 'organizer/clients/list.html'

    def get_context_data(self, **kwargs):
        # request should not be None, TemplateViewSimple ensures this
        context = super(ClientList, self).get_context_data(**kwargs)

        clients = organizer_models.Client.objects.filter(Q(user=self.request.user) | Q(limited=False))
        context['clients'] = clients.all()

        return context

class ClientEditMixin:
    template_name = 'organizer/generic_forms/edit_form.html'
    form_class = organizer_forms.ClientForm
    model = organizer_models.Client
    success_url = reverse_lazy('clients.list')
class ClientEdit(ClientEditMixin, UpdateView):
    pass
class ClientCreate(ClientEditMixin, CreateView):
    pass
class ClientDelete(ClientEditMixin, DeleteView):
    template_name = 'organizer/clients/delete_form.html'
