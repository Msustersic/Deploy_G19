from django.contrib import admin
from django.contrib.admin import ModelAdmin


from .models import Store

@admin.register(Store)
class StoresAdmin(ModelAdmin):
    ...
