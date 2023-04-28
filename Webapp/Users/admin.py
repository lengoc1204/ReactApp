from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name', 'email')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
