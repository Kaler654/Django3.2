from django.db import models
from django.core import validators
from .validators import validate_brilliant
from core.models import BaseMixin, SlugMixin


class Item(BaseMixin):
    name = models.CharField(verbose_name="Название",
                            max_length=150,
                            help_text="Допустимая длина 150 символов")

    text = models.TextField(verbose_name="Описание",
                            help_text="Минимум два слова",
                            validators=[validate_brilliant])

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Tag(SlugMixin, BaseMixin):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(SlugMixin, BaseMixin):
    weight = models.PositiveSmallIntegerField(verbose_name="Вес", default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
