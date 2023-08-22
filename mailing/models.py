from django.db import models


class Client(models.Model):
    email = models.CharField(max_length=150, verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)


    def __str__(self):
        return f'{self.full_name} {self.email}'


    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('full_name',)


