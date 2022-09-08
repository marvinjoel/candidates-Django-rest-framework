from django.contrib import admin

from candidates.presidency.models import PresidencyModel, Studies, PoliticModel

admin.site.register(PresidencyModel)
admin.site.register(Studies)
admin.site.register(PoliticModel)
