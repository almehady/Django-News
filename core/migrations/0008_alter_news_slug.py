# Generated by Django 3.2.4 on 2021-12-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211231_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]