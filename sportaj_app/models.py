from django.db import models
from django.contrib.postgres.fields import ArrayField

from taggit.managers import TaggableManager


def get_header_images_default():
    # TODO: Use proper placeholder image
    return list(['http://www.atletski-klub-poljane.si/wp-content/themes/poljane/images/header/8.jpg'])


class Klub(models.Model):
    slug = models.SlugField(unique=True)
    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)
    logo = models.URLField()
    header_images = ArrayField(
        models.URLField(default=''),
        verbose_name='Header Images',
        name='header_images',
        default=get_header_images_default
    )

    tags = TaggableManager()

    class Meta:
        verbose_name = 'Klub'
        verbose_name_plural = 'Klubi'

    def __str__(self):
        return self.ime
