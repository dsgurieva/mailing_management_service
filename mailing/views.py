from django.http import Http404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from blog.models import Blog
from mailing.models import MailingSettings, Client, MessageSend, MailingLogs
from django.urls import reverse_lazy
from mailing.forms import MailingSettingsForm, ClientSettingsForm, MessageSendForm, MailingSettingsManagerForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MailingListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    template_name = 'mailing/mailing_list.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing'] = MailingSettings.objects.all().count()
        context_data['count_mailing_active'] = MailingSettings.objects.filter(
            status=3).count()
        context_data['count_unique_customers'] = Client.objects.distinct().count()
        context_data['title'] = 'Главная страница рассылок'
        context_data['blog'] = Blog.objects.all()[:3]
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
    success_url = reverse_lazy('mailing:create_mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_class(self):
        user = self.request.user
        mailing = self.object
        if mailing.user == user or user.is_superuser:
            self.form_class = MailingSettingsForm
            return self.form_class
        elif mailing.user == user and user.is_staff:
            self.form_class = MailingSettingsForm
            return self.form_class
        else:
            self.form_class = MailingSettingsManagerForm
            return self.form_class


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageSendListView(LoginRequiredMixin, ListView):
    model = MessageSend
    template_name = 'mailing/mailing_list.html'
    success_url = reverse_lazy('mailing:mailing_list')


class MessageSendListView(LoginRequiredMixin, ListView):
    model = MessageSend
    template_name = 'mailing/messagesend_list.html'
    success_url = reverse_lazy('mailing:message_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.view_mailingmessage'):
            return queryset
        return super().get_queryset().filter(user=self.request.user)


class MessageSendCreateView(LoginRequiredMixin, CreateView):
    model = MessageSend
    form_class = MessageSendForm
    template_name = 'mailing/messagesend_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageSendUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageSend
    form_class = MessageSendForm
    template_name = 'mailing/messagesend_form.html'
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageSendDetailView(LoginRequiredMixin, DetailView):
    model = MessageSend


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mailing/client_list.html'
    success_url = reverse_lazy('mailing:client')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientSettingsForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientSettingsForm
    template_name = 'mailing/client_form.html'
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MailingLogsListView(ListView):
    model = MailingLogs

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing_list.view_mailinglog'):
            return queryset
        return queryset.filter(user=self.request.user)

