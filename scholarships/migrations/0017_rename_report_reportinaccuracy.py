# Generated by Django 5.0.2 on 2024-02-21 14:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0016_report'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Report',
            new_name='ReportInaccuracy',
        ),
    ]
