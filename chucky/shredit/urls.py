from django.urls import path
from . import views


app_name = 'shredit'

urlpatterns = [
    path("", views.index, name='index-page'),
    path("dashboard/", views.home, name='dashboard'),
    path("about/", views.about_us, name='about'),
    path("contact/", views.contact_us, name='contact'),
    path("documentation/", views.docs_page, name='docs'),
    path("download/<int:id>/", views.download, name='download'),
    path("share/", views.share_page, name='share')
]
