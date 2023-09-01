from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='заголовок')
    content_article = models.TextField(verbose_name='содержание статьи')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', null=True, blank=True)
    date_of_creation = models.DateField(verbose_name='дата создания', null=True, blank=True)
    view_count = models.IntegerField(default=0, verbose_name='просмотры')


    def __str__(self):
        return self.heading


    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
