from django.contrib import admin
from .models import Cupon

# Register your models here.
@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo']
