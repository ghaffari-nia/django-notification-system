# Generated by Django 3.1.3 on 2020-12-01 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_notification_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='notification_creator_module',
            new_name='notification_module_name',
        ),
    ]