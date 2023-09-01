from django import forms
from mailing.models import MailingSettings, MessageSend


class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = ('client',)


class MessageSendForm(forms.ModelForm):

    class Meta:
        model = MessageSend
        exclude = '__all__'