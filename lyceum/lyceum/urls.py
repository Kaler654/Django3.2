from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('catalog.urls')),
    path('', include('about.urls')),
    path('auth/', include('users.urls')),
]
