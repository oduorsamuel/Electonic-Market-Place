from django.contrib import admin
from .models import UserModel


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


admin.site.register(UserModel, UserAdmin)
