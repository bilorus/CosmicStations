from django.contrib import admin

from .models import *


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition', 'time_create', 'time_broke')


admin.site.register(Station, StationAdmin)
admin.site.register(Indication)
