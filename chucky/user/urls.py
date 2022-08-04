from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.signin_view, name='user-login'),
    path('logout/', views.signout_view, name='user-logout')
]