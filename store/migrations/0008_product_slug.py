# Generated by Django 3.2.25 on 2025-02-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_delete_shopcollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, editable=False, max_length=200, null=True),
        ),
    ]
