# Generated by Django 4.1.3 on 2022-12-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_mall_api', '0002_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mall',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
