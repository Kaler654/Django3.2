from django.shortcuts import render


def item_list(request):
    template = "catalog/item_list.html"
    context = {}
    return render(request, template, context=context)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    context = {}
    return render(request, template, context=context)
