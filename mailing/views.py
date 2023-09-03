from django.forms import inlineformset_factory
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from mailing.models import MailingSettings, MessageSend, Client
from django.urls import reverse_lazy
from mailing.forms import MailingSettingsForm, MessageSendForm, ClientSettingsForm


class MailingListView(ListView):
    model = MailingSettings
    template_name = 'mailing/mailing_list.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        messagesend_formset = inlineformset_factory(MailingSettings, MessageSend, form=MessageSendForm, extra=1)
        context_data['formset'] = messagesend_formset()
        return context_data


class MailingUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = MailingSettings


class MailingDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'
    success_url = reverse_lazy('mailing:client')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientSettingsForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientSettingsForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')