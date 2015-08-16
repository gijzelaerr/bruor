from django.contrib import admin
from .models import Malt, Hop

class MaltAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'color', 'gravity')


class HopAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'alpha_min', 'alpha_max')


admin.site.register(Malt, MaltAdmin)
admin.site.register(Hop, HopAdmin)
