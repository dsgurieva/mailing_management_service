from django import forms
from mailing.models import MailingSettings, MessageSend, Client


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = '__all__'
        #exclude = ('client',)


class MessageSendForm(forms.ModelForm):
    class Meta:
        model = MessageSend
        #fields = '__all__'
        exclude = ('user',)


class ClientSettingsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSettingsManagerForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('status',)
