from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('url_shortener.urls', namespace='short')),
    path('admin/', admin.site.urls),
]
