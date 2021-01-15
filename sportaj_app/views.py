from django.views.generic.base import TemplateView

from sportaj_app import models
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
        except models.Klub.DoesNotExist:
            raise Http404("Klub ne obstaja")
        return context
