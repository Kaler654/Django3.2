from django.shortcuts import render


def item_list(request):
    template = "catalog/item_list.html"
    return render(request, template)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    return render(request, template)
