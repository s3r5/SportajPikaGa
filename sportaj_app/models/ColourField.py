from django.db import models


class ColourField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 32)
        super().__init__(*args, **kwargs)
