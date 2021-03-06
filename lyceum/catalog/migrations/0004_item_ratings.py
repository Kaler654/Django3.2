# Generated by Django 3.2 on 2022-03-26 09:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rating", "0001_initial"),
        ("catalog", "0003_auto_20220326_1238"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="ratings",
            field=models.ManyToManyField(
                related_name="items",
                through="rating.Rating",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Оценки",
            ),
        ),
    ]
