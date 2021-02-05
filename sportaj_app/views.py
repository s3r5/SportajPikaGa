from django.views.generic.base import TemplateView

import json
from sportaj_app import models
from django.conf import settings
from django.http import Http404, HttpResponse


class HomeView(TemplateView):
    template_name = "sportaj/base.html"


class KlubView(TemplateView):
    template_name = "sportaj/klub.html"
    model = models.Klub

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context["klub"] = models.Klub.objects.get(slug=kwargs["slug"])
            context["headerSlike"] = models.SlikaKluba.objects.filter(klub=context["klub"])
            context["GOOGLE_CAL_API_KEY"] = settings.GOOGLE_CAL_API_KEY
        except models.Klub.DoesNotExist or not context["headerSlike"]:
            raise Http404("Klub ne obstaja")
        return context


class ZemljevidView(TemplateView):
    template_name = "sportaj/zemljevid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ime = self.request.GET.get("ime", "")
        klubi = (models.Klub.objects.all(), models.Klub.objects.filter(ime__icontains=ime))[ime != ""]

        context["GOOGLE_SEARCH_MAPS_API_KEY"] = settings.GOOGLE_SEARCH_MAPS_API_KEY
        context["DEFAULT_LATLONG"] = models.get_location_city_default()
        context["klubi"] = [
            dict(
                latlong=k.location.split(","),
                location=k.location_friendly,
                ime=k.ime,
                opis=k.opis,
                slug=k.slug,
                logo=k.logo
            ) for k in klubi
        ]

        return context
