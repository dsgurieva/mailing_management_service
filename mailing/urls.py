from django.urls import path
from mailing.views import MailingCreateView, MailingUpdateView, MailingDetailView, MailingListView, MailingDeleteView, \
    ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView
from mailing.apps import MailingConfig


app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='detail_mailing'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('client', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_mailing'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client_view/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]