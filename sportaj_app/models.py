from django.db import models

from taggit.managers import TaggableManager


class Klub(models.Model):
    slug = models.SlugField()
    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)
    logo = models.URLField()

    tags = TaggableManager()

    class Meta:
        verbose_name = 'Klub'
        verbose_name_plural = 'Klubi'

    def __str__(self):
        return self.ime
