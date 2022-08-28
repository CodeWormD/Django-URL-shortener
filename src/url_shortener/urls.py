from django.urls import path
from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('', views.create, name='index'),
]