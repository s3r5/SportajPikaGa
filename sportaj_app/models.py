from django.db import models

import os
from PIL import Image
from location_field.models.plain import PlainLocationField
from taggit.managers import TaggableManager


def get_header_images_default(): list([])


def get_location_city_default():
    return "46.55472,15.64667"


class Klub(models.Model):
    slug = models.SlugField(unique=True)

    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)

    logo = models.ImageField(upload_to="klub_logo/", blank=True)

    location = PlainLocationField(
        based_fields=["city"], default=get_location_city_default()
    )

    urnik = models.CharField(max_length=512, null=True, blank=True)

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


class SlikaKluba(models.Model):
    naslov = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)
    slika = models.ImageField(upload_to="header_slike/")

    klub = models.ForeignKey(Klub, on_delete=models.CASCADE, related_name="slike")

    class Meta:
        verbose_name = "Slika"
        verbose_name_plural = "Slike"

    def save(self, *args, **kwargs):
        super(SlikaKluba, self).save(*args, **kwargs)

        image = Image.open(self.slika.path).convert("RGB")

        image.save(os.path.splitext(self.slika.path)[0] + ".webp", "webp", lossless=False, quality=50)

        self.slika = os.path.splitext(self.slika.name)[0] + ".webp"
        super(SlikaKluba, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.klub, self.naslov)
