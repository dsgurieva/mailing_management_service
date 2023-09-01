from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from mailing.models import MailingSettings, MessageSend
from django.urls import reverse_lazy
from mailing.forms import MailingSettingsForm, MessageSendForm


def index(request):
    return render(request, 'mailing/index.html')


class MailingCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
    success_url = reverse_lazy('mailing:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        messagesend_formset = inlineformset_factory(MailingSettings, MessageSend, form=MessageSendForm, extra=1)
        context_data['formset'] = messagesend_formset()
        return context_data


class MailingUpdateView(UpdateView):
    pass