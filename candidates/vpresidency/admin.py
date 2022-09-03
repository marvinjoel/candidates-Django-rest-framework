from django.contrib import admin

from candidates.vpresidency.models import ParAndinoModel, CongresistaModel

admin.site.register(CongresistaModel)
admin.site.register(ParAndinoModel)
