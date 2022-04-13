from django.shortcuts import get_object_or_404, render, redirect

from catalog.models import Category, Item
from django.db.models import Avg, Count
from rating.models import Rating


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.published_items_and_categories()
    items = sorted(items, key=lambda x: x.category.weight, reverse=True)
    context = {"items": items}
    return render(request, template, context=context)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    items = Item.objects.published_item_and_tags()
    item = get_object_or_404(Item, pk=catalog_id)
    if request.method == "GET":
        star_list = Rating.choices
        stars = Rating.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(
            Avg("star"), Count("star")
        )
        if request.user.is_authenticated:
            try:
                user_star = Rating.objects.get(item=item, user=request.user).star
            except Rating.DoesNotExist:
                user_star = 0
        else:
            user_star = 0

        context = {
            "item": item,
            "star_dict": star_list,
            "stars": stars,
            "user_star": user_star,
        }
        return render(request, template, context=context)

    elif request.method == "POST":
        if (
            request.POST["rate"] in ["0", "1", "2", "3", "4", "5"]
            and request.user.is_authenticated
        ):
            obj, created = Rating.objects.get_or_create(
                user=request.user,
                item=item,
                defaults={
                    "item": item,
                    "user": request.user,
                },
            )

            obj.star = int(request.POST["rate"])
            obj.save()
        return redirect("item_detail", catalog_id=catalog_id)
