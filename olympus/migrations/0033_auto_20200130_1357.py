# Generated by Django 2.2.4 on 2020-01-30 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0032_favpagepost_favpage_post_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favpagepostusercomment',
            old_name='favpage_post_comment',
            new_name='comment',
        ),
    ]
