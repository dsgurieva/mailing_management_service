from django import forms
from mailing.models import MailingSettings, MessageSend, Client


class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = ('client',)


class MessageSendForm(forms.ModelForm):

    class Meta:
        model = MessageSend
        exclude = '__all__'


class ClientSettingsForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = '__all__'