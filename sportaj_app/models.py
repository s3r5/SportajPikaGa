from django.db import models
from django.contrib.postgres.fields import ArrayField
from location_field.models.plain import PlainLocationField

from taggit.managers import TaggableManager


def get_header_images_default():
    # TODO: Use proper placeholder image
    return list(
        [
            "http://www.atletski-klub-poljane.si/wp-content/themes/poljane/images/header/8.jpg",
            "http://share.quantumlytangled.com/7DxO55p5",
        ]
    )


def get_location_city_default():
    return "Maribor"


class Klub(models.Model):
    slug = models.SlugField(unique=True)

    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)

    logo = models.URLField()
    header_images = ArrayField(
        models.URLField(verbose_name="Header Image", name="header_image", default=None),
        verbose_name="Header Images",
        name="header_images",
        default=get_header_images_default,
    )

    city = models.CharField(max_length=1023, default=get_location_city_default())
    location = PlainLocationField(
        based_fields=["city"], default=get_location_city_default()
    )

    mail = models.EmailField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)

    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)

    tags = TaggableManager()

    class Meta:
        verbose_name = "Klub"
        verbose_name_plural = "Klubi"

    def __str__(self):
        return self.ime
