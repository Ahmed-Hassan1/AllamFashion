# Generated by Django 3.2.25 on 2025-02-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_websiteinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinfo',
            name='Logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
