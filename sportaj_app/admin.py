from django.contrib import admin

from .models import Klub, SlikaKluba


class SlikaKlubaAdmin(admin.StackedInline):
    model = SlikaKluba

@admin.register(Klub)
class KlubAdmin(admin.ModelAdmin):
    inlines = [
        SlikaKlubaAdmin
    ]

    class Meta:
        model = Klub

@admin.register(SlikaKluba)
class SlikaKlubaAdmin(admin.ModelAdmin):
    pass
