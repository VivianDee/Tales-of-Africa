# Generated by Django 4.2.6 on 2023-12-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africanlibrary', '0002_alter_story_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.IntegerField(default=-1),
        ),
    ]
