from django.contrib import admin
from .models import Flower, Sighting, Use

# Register your models here.
admin.site.register(Flower)
admin.site.register(Sighting)
admin.site.register(Use)