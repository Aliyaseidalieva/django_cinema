from django.contrib import admin

from .models import Rating, RatingStar

admin.site.register(RatingStar)
admin.site.register(Rating)
