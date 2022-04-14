from django.shortcuts import get_object_or_404, render, redirect

from catalog.models import Category, Item
from django.db.models import Avg, Count
from rating.models import Rating
from django import forms


class FeedbackForm(forms.Form):
    choices = Rating.choices


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.published_items_and_categories()
    items = sorted(items, key=lambda x: x.category.weight, reverse=True)
    context = {"items": items}
    return render(request, template, context=context)


def item_detail(request, catalog_id):
    template = "catalog/item_detail.html"
    items = Item.objects.published_item_and_tags()
    item = get_object_or_404(items, pk=catalog_id)
    form = FeedbackForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if "rate" in request.POST and request.POST["rate"].isdigit():
            rate = int(request.POST["rate"])
            rating_choices = list(map(lambda x: x[0], Rating.choices))
            if rate in rating_choices and request.user.is_authenticated:
                Rating.objects.update_or_create(
                    item=item, user=request.user, defaults={"star": rate}
                )
        return redirect("item_detail", catalog_id=catalog_id)

    star_list = Rating.choices
    stars = item.item_stars.exclude(star=0).aggregate(Avg("star"), Count("star"))

    user_star = 0
    if request.user.is_authenticated:
        user_rate = Rating.objects.filter(item=item, user=request.user).first()
        if user_rate:
            user_star = user_rate.star

    context = {
        "item": item,
        "star_dict": star_list,
        "stars": stars,
        "user_star": user_star,
    }
    return render(request, template, context=context)
