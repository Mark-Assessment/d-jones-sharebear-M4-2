# Generated by Django 3.2.18 on 2023-05-18 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=254, null=True)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('attendees', models.ManyToManyField(related_name='events_attending', to=settings.AUTH_USER_MODEL)),
                ('interested', models.ManyToManyField(related_name='events_interested', to=settings.AUTH_USER_MODEL)),
                ('organiser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
