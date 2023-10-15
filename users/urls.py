from django.urls import path
from django.views.decorators.cache import never_cache
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, activate_new_user

app_name = UsersConfig.name


urlpatterns = [
    path('', never_cache(LoginView.as_view()), name='login'),
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('activate/<int:pk>/', never_cache(activate_new_user), name='activate'),
]