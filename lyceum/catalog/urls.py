from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    path('catalog/', item_list),
    path('catalog/<int:catalog_id>/', item_detail),
]
