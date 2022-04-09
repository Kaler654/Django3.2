from django.shortcuts import render, get_object_or_404
from catalog.models import Item, Category
from random import shuffle


def item_list(request):
    template = "catalog/item_list.html"
    categories = Category.objects.published_category_and_items().order_by('weight')
    context = {
        'categories': categories
    }
    return render(request, template, context=context)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    item = get_object_or_404(Item, pk=catalog_id)
    context = {"item": item}
    return render(request, template, context=context)
