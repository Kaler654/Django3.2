# Generated by Django 3.2 on 2022-04-13 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_auto_20220408_2328"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("weight",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
