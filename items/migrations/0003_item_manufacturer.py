# Generated by Django 3.2.18 on 2023-04-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20230420_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
