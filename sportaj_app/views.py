from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "sportaj/base.html"


class KlubView(TemplateView):
    template_name = "sportaj/klub.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
