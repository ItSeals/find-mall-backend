# Generated by Django 4.1.5 on 2023-01-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_mall_api', '0014_alter_mall_mall_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall',
            name='mall_image',
            field=models.ImageField(blank=True, default='src/image.jpg', null=True, upload_to=None),
        ),
    ]