from django.db import models
from django.contrib.auth.admin import User
from .validators import validate_brilliant
from core.models import BaseMixin, SlugMixin
from django.db.models import Prefetch


class ItemManager(models.Manager):
    def published_item_and_tags(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                "tags",
                queryset=Tag.objects.filter(is_published=True),
            )
        )


class Item(BaseMixin):
    name = models.CharField(
        verbose_name="Название",
        max_length=150,
        help_text="Допустимая длина 150 символов",
    )
    text = models.TextField(
        verbose_name="Описание",
        help_text="Минимум два слова",
        validators=[validate_brilliant],
    )
    category = models.ForeignKey(
        verbose_name="Категория",
        to="Category",
        related_name="items",
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(
        verbose_name="Теги",
        to="Tag",
        related_name="items",
    )
    ratings = models.ManyToManyField(
        verbose_name="Оценки",
        to=User,
        related_name="items",
        through="rating.Rating",
        through_fields=("item", "user"),
    )

    objects = ItemManager()

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("name",)


class Tag(SlugMixin, BaseMixin):
    name = models.CharField(verbose_name="Название", max_length=255, default="")

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class CategoryManager(models.Manager):
    def published_category_and_items(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch("items", queryset=Item.objects.published_item_and_tags())
        )


class Category(SlugMixin, BaseMixin):
    name = models.CharField(verbose_name="Название", max_length=255, default="")
    weight = models.PositiveSmallIntegerField(verbose_name="Вес", default=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
