from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register_view, forgot_view, \
    register_activate_email, forgot_activate_email, reset_password, send_message, log_out

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', log_out, name='logout'),
    path('forgot', forgot_view, name='forgot_view'),

    path('activate-register/<str:uid>/<str:token>',register_activate_email),
    path('activate-forgot/<str:uid>/<str:token>',forgot_activate_email),
    path('reset-password',reset_password,name='reset_password'),
    path('message/',send_message,name='message')
]
