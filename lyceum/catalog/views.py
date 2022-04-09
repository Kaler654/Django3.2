from django.shortcuts import render, get_object_or_404
from catalog.models import Item, Tag
from random import shuffle


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.published_item_and_tags()
    context = {
        "items": items,
    }
    return render(request, template, context=context)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    item = get_object_or_404(Item, pk=catalog_id)
    context = {"item": item}
    return render(request, template, context=context)
