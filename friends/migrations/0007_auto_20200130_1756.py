# Generated by Django 2.2.4 on 2020-01-30 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_auto_20200130_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fgrouppostcomment',
            old_name='FGroup_post_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='fgrouppostcomment',
            old_name='FGroup_post',
            new_name='post',
        ),
    ]