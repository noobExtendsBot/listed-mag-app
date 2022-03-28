from django.contrib import admin
from .models import CustomUser, CustomAccountManager

# Register your models here.


class AdminCustomUser(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    search_fields = ('email', 'first_name', 'last_name',)


admin.site.register(CustomUser, AdminCustomUser)