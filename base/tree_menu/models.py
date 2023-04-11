import json

from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Menu title')
    slug = models.CharField(max_length=100, verbose_name='Menu slug')
    description = models.CharField(max_length=256, verbose_name='Menu description')

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        verbose_name='menu',
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='items',
        verbose_name='parent menu item',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, verbose_name='Menu item title')
    url = models.CharField(
        max_length=255,
        verbose_name='Link',
        blank=True,
        null=True,
    )
    named_url = models.CharField(
        max_length=255,
        verbose_name='Named URL',
        blank=True,
        null=True,
    )
    named_url_kwargs = models.CharField(
        max_length=255,
        verbose_name='Named URL kwargs',
        blank=True,
        null=True,
        help_text='As JSON',
    )

    def get_url(self):
        if self.url:
            return self.url
        if self.named_url_kwargs:
            kwargs = json.loads(self.named_url_kwargs)
            return reverse(self.named_url, kwargs=kwargs)
        if self.named_url:
            return reverse(self.named_url)
        return '/#'

    def __str__(self):
        return self.title
