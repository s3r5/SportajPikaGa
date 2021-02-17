from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase
from colorfield.fields import ColorField
from faicon.fields import FAIconField
from django.contrib import admin
from taggit.admin import TagAdmin


class CustomTag(TagBase):
    colour = ColorField(default="#2643E9FF", format="hexa")
    icon = FAIconField(blank=True)

    class Meta:
        verbose_name = _("Custom tag")
        verbose_name_plural = _("Custom tags")


class CustomTaggedItem(TaggedItemBase):
    content_object = models.ForeignKey("Klub", on_delete=models.CASCADE)

    class Meta:
        abstract = True


def custom_tag_field(module, model_name, name, related_name, tag_base_class=CustomTag):
    tag_cls = type(
        name + "Tag",
        (tag_base_class,), {
            "__module__": module,
        }
    )

    tagged_item_cls = type(
        "TaggedItem" + name,
        (CustomTaggedItem,), {
            "__module__": module,
            "tag_class": tag_cls,
            "content_object": models.ForeignKey(model_name, on_delete=models.CASCADE),
            "tag": models.ForeignKey(
                tag_cls,
                on_delete=models.CASCADE,
                related_name="%(app_label)s_%(class)s_items",
            ),
            "Meta": type("Meta", (), {})
        }
    )

    return TaggableManager(through=tagged_item_cls, related_name=related_name, verbose_name=name)


def custom_tag_inline(tagged_item_cls):
    inline_cls = type(
        tagged_item_cls.__name__ + "Inline",
        (admin.StackedInline,), {
            "model": tagged_item_cls
        })
    return inline_cls


def custom_tag_admin(tagged_item_cls):
    admin_cls = type(
        tagged_item_cls.__name__ + "Admin",
        (TagAdmin,), {
            "inlines": [custom_tag_inline(tagged_item_cls)]
        })
    return admin_cls


def custom_tag_register_admin(tagged_item_cls):
    cls = custom_tag_admin(tagged_item_cls)
    admin.site.register(tagged_item_cls.tag_model(), cls)
