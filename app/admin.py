from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hall)
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Event)