# Generated by Django 2.2.4 on 2020-01-08 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olympus', '0025_favouritepages'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavouritePages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_page_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olympus.FavouritePages')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
