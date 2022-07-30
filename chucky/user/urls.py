from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]