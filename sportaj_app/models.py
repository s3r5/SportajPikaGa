from django.db import models


class Klub(models.Model):
    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)

    class Meta:
        verbose_name = 'Klub'
        verbose_name_plural = 'Klubi'

    def __str__(self):
        return self.ime
