from django.contrib import admin
from mailing.models import Client, MessageSend, MailingSettings, MailingLogs


@admin.register(Client)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)


admin.site.register(MessageSend)


admin.site.register(MailingSettings)


admin.site.register(MailingLogs)