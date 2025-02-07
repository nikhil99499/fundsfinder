# Generated by Django 5.0.2 on 2024-02-14 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0012_scholarshipapplication_approved_scholarship'),
        ('userprofile', '0007_remove_userprofile_scholarships_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='userprofile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='userprofile.userprofile'),
        ),
        migrations.AddField(
            model_name='scholarshipapplication',
            name='userprofile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scholarships', to='userprofile.userprofile'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scholarshipapplication',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
