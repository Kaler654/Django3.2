from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("auth/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [path("__debug__/", include("debug_toolbar.urls"))]
