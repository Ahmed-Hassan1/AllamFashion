# Generated by Django 3.2.25 on 2025-03-03 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
