# Generated by Django 5.0.2 on 2024-02-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_rename_user_notification_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
