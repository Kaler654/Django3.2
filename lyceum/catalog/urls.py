from django.urls import path

from .views import item_detail, item_list

urlpatterns = [
    path("", item_list),
    path("<int:catalog_id>/", item_detail, name="item_detail"),
]
