# Generated by Django 4.0.5 on 2022-06-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='site',
            new_name='sites',
        ),
        migrations.AddField(
            model_name='site',
            name='file',
            field=models.ManyToManyField(to='demoapp.upload'),
        ),
    ]