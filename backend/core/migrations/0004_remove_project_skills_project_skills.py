# Generated by Django 4.1.7 on 2023-10-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_project_app_video_delete_apppictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='core.skill'),
        ),
    ]
