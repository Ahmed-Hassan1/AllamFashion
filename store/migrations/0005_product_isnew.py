# Generated by Django 3.2.25 on 2025-02-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isNew',
            field=models.BooleanField(default=False),
        ),
    ]
