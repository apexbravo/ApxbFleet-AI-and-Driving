# Generated by Django 4.1.3 on 2023-04-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApxbFleetMain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='driver',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]