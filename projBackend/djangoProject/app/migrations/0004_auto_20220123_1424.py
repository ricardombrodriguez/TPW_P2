# Generated by Django 2.2.12 on 2022-01-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220123_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication_status',
            old_name='active',
            new_name='enabled',
        ),
    ]
