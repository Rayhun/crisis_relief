from django.contrib import admin
from .models import Request

admin.site.register(Request)

from .models import Offer
admin.site.register(Offer)
