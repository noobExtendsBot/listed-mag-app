from django.contrib import admin
from .models import MagazinePost


# Register your models here.

class AdminMagazinePost(admin.ModelAdmin):
    list_display = ('title', 'description', 'uploaded_at')
    ordering = ('-uploaded_at',)
    search_fields = ('title', 'description',)
    list_filter = ('title', 'uploaded_at',)


admin.site.register(MagazinePost, AdminMagazinePost)