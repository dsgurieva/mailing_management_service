from django.core.mail import send_mail
from django.conf import settings
import datetime
from smtplib import SMTPException
from mailing.models import MailingSettings, MailingLogs


def _send_email(message_settings, message_client):
    result_txt = ('Успешно отправлено')
    try:
        result = send_mail(
            subject=message_settings.message.letter_subject,
            message=message_settings.message.letter_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[message_client.client.email],
            fail_silently=False
        )
    except SMTPException:
        result_txt = ('Во время отправки возникла ошибка')

    MailingLogs.objects.create(
        status=MailingLogs.STATUS_OK if result else MailingLogs.STATUS_FAILED,
        mailing=message_settings,
        client_id=message_client.client_id,
        mailing_service_response=result_txt
    )


def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc).time()
    for mailing_settings in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
        if (datetime_now > mailing_settings.time) and (datetime_now < mailing_settings.time):
            for mailing_client in mailing_settings.mailingclient_set.all():
                mailing_log = MailingLogs.objects.filter(
                    client=mailing_client.client,
                    mailing=mailing_settings
                )
                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_attempt').first().last_attempt

                    if mailing_settings.periodicity == MailingSettings.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_email(mailing_settings, mailing_client)
                        elif mailing_settings.periodicity == MailingSettings.PERIOD_WEEKLY:
                            if (datetime_now - last_try_date).days >= 7:
                                _send_email(mailing_settings, mailing_client)
                        elif mailing_settings.periodicity == MailingSettings.PERIOD_MONTHLY:
                            if (datetime_now - last_try_date).days >= 30:
                                _send_email(mailing_settings, mailing_client)
                else:
                    _send_email(mailing_settings, mailing_client)