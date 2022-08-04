from django.urls import path
from . import views


app_name = 'shredit'

urlpatterns = [
    path("", views.index, name='index-page'),
    path("dashboard/", views.home, name='dashboard'),

]