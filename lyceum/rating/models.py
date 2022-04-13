from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


class Rating(models.Model):
    choices = (
        (0, "Ещё не оценили"),
        (1, "Ненависть"),
        (2, "Неприязнь"),
        (3, "Нейтрально"),
        (4, "Обожание"),
        (5, "Любовь"),
    )
    star = models.IntegerField(verbose_name="Оценка", choices=choices, default=0)
    item = models.ForeignKey(
        verbose_name="Товар",
        to="catalog.Item",
        on_delete=models.CASCADE,
        related_name="item_stars",
    )
    user = models.ForeignKey(
        verbose_name="Пользователь",
        to=User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        constraints = [
            UniqueConstraint(
                fields=(
                    "item",
                    "user",
                ),
                name="unique_rating",
            )
        ]
