from django.views.generic.base import TemplateView

from sportaj_app import models
from django.conf import settings
from django.http import Http404


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
