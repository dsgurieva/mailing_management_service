from django.urls import path
from mailing.views import index, MailingCreateView, MailingUpdateView
from mailing.apps import MailingConfig



app_name = MailingConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    #path('update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
]