from django import template
from geopy.geocoders import Nominatim

register = template.Library()
geolocator = Nominatim(user_agent="sportaj.ga")

@register.filter(name='latlongHuman')
def latlongHuman(value):
    return geolocator.reverse(value).address
