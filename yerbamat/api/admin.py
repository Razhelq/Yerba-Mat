from django.contrib import admin
from api.models import Log


@admin.register(Log)
class Log(admin.ModelAdmin):
    readonly_fields = ('date',)