from django import forms
from mailing.models import MailingSettings, MessageSend, Client


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        exclude = ('user',)



class MessageSendForm(forms.ModelForm):
    class Meta:
        model = MessageSend
        exclude = ('user',)


class ClientSettingsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingsManagerForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('status',)
