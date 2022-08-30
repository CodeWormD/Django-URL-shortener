from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('url_shortener.urls', namespace='short')),
    path('admin/', admin.site.urls),
]
