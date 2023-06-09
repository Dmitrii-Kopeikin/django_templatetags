# Generated by Django 4.2 on 2023-04-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0003_menuitem_named_url_kwargs_alter_menuitem_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='description', max_length=256, verbose_name='Menu description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='named_url_kwargs',
            field=models.CharField(blank=True, help_text='As JSON', max_length=255, null=True, verbose_name='Named URL kwargs'),
        ),
    ]
