from django.urls import path

from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('a/', views.create, name='create'),
    path('s/<slug:link>/', views.redir, name='redir'),
]
