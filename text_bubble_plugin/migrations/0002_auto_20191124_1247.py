# Generated by Django 2.2.3 on 2019-11-24 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_bubble_plugin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textmodel',
            old_name='text',
            new_name='content',
        ),
    ]
