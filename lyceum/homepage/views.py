from random import shuffle

from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = "homepage/home.html"
    items_ids = list(
        Item.objects.filter(is_published=True).values_list("id", flat=True)
    )
    shuffle(items_ids)
    if items_ids:
        items = Item.objects.published_item_and_tags().filter(id__in=items_ids[:3])
    else:
        items = None
    context = {
        "items": items,
    }
    return render(request, template, context=context)
