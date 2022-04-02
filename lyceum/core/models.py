from django.db import models


class BaseMixin(models.Model):
    is_published = models.BooleanField(
        verbose_name="Опубликованно",
        default=True
    )

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        verbose_name="Название",
        max_length=200, unique=True,
        help_text="Допустимая длина 200 символов"
    )

    class Meta:
        abstract = True
