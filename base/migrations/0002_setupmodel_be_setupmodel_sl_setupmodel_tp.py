# Generated by Django 4.0.1 on 2022-04-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setupmodel',
            name='be',
            field=models.BooleanField(default=False, verbose_name='be'),
        ),
        migrations.AddField(
            model_name='setupmodel',
            name='sl',
            field=models.BooleanField(default=False, verbose_name='sl'),
        ),
        migrations.AddField(
            model_name='setupmodel',
            name='tp',
            field=models.BooleanField(default=False, verbose_name='tp'),
        ),
    ]