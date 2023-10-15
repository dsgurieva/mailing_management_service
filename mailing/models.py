from django.db import models
from django.conf import settings


class Client(models.Model):
    email = models.CharField(max_length=150, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='пользователь')


    def __str__(self):
        return f'{self.full_name} {self.email}'


    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('full_name',)


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'


    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )


    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    time = models.TimeField(verbose_name='время рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='переодичность рассылки')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиент')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='пользователь')


class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


class MessageSend(models.Model):
    letter_subject = models.CharField(max_length=150, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма')
    mailing = models.OneToOneField(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='пользователь')


    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLogs(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )


    datetime = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус попытки')
    client = models.OneToOneField(Client, on_delete=models.CASCADE, verbose_name='клиент')
    mailing = models.OneToOneField(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='пользователь')


    class Meta:
            verbose_name = 'лог рассылки'
            verbose_name_plural = 'логи рассылки'

