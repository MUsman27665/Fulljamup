# Generated by Django 2.2.4 on 2020-02-17 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200115_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='political_incline',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='relationship_status',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='religious_belifs',
        ),
    ]