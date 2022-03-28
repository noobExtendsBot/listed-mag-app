from django.contrib import admin
from .models import Add


# Register your models here.

class AddsAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'published_date',)
    ordering = ('priority',)
    search_fields = ('title',)
    list_filter = ('priority', 'published_date',)


admin.site.register(Add, AddsAdmin)