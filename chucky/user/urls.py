from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.signin_view, name='user-login'),
    path('logout/', views.signout_view, name='user-logout'),

    # reset password urls
    path('password-reset/', auth_view.PasswordResetView.as_view(
        email_template_name='user/pass_reset_email.html',
        template_name='user/pas_reset_form.html',
        success_url=reverse_lazy('user:password_reset_done')),
        name='password_reset'
    ),

    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(
             template_name='user/pass_reset_confirm.html',
             success_url=reverse_lazy('user:password_reset_complete')),
         name='password_reset_confirm'),

    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(
             template_name='user/pass_reset_done.html'),
         name='password_reset_done'),

    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(
             template_name='user/pass_complete.html'),
         name='password_reset_complete'),

]
