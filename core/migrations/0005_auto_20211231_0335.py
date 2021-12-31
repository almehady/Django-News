# Generated by Django 3.2.4 on 2021-12-30 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_news_quote_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maincategory',
            options={'ordering': ['-created_at'], 'verbose_name': 'Main Category', 'verbose_name_plural': 'Main Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='maincategory',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='maincategory',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
