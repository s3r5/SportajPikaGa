from django.contrib import admin
from django import forms
from taggit_labels import widgets

from .models import Klub, SlikaKluba, PanogeManager, VadbeManager, StarostiManager, SpoliManager
from .tags import custom_tag_register_admin


class KlubAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["panoge_tags"].widget = widgets.LabelWidget(model=Klub.panoge_tags.through.tag_class)
        self.fields["vadbe_tags"].widget = widgets.LabelWidget(model=Klub.vadbe_tags.through.tag_class)
        self.fields["starosti_tags"].widget = widgets.LabelWidget(model=Klub.starosti_tags.through.tag_class)
        self.fields["spoli_tags"].widget = widgets.LabelWidget(model=Klub.spoli_tags.through.tag_class)

    class Meta:
        model = Klub
        fields = [
            "ime",
            "opis",
            "logo",
            "location",
            "urnik",
            "mail",
            "homepage",
            "twitter",
            "facebook",
            "panoge_tags",
            "vadbe_tags",
            "starosti_tags",
            "spoli_tags"
        ]

class SlikaKlubaAdmin(admin.StackedInline):
    model = SlikaKluba

@admin.register(Klub)
class KlubAdmin(admin.ModelAdmin):
    form = KlubAdminForm
    inlines = [
        SlikaKlubaAdmin
    ]

    class Meta:
        model = Klub

@admin.register(SlikaKluba)
class SlikaKlubaAdmin(admin.ModelAdmin):
    pass


custom_tag_register_admin(PanogeManager.through)
custom_tag_register_admin(VadbeManager.through)
custom_tag_register_admin(StarostiManager.through)
custom_tag_register_admin(SpoliManager.through)
