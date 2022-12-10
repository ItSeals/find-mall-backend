# Generated by Django 4.1.3 on 2022-12-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_mall_api', '0004_alter_categories_created_at_alter_mall_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField(max_length=1800)),
                ('status', models.IntegerField()),
                ('mall_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]