# Generated by Django 4.1.3 on 2022-12-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_mall_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='mall',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='mall',
            name='updated_at',
        ),
    ]
