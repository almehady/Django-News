# Generated by Django 3.2.4 on 2021-12-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211231_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='quote_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
