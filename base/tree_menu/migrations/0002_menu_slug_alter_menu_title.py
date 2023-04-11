# Generated by Django 4.2 on 2023-04-10 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Menu slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Menu title'),
        ),
    ]