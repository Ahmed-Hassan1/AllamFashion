# Generated by Django 3.2.25 on 2025-02-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_isnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
