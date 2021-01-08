from django.contrib import admin
from .models import Articles


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ()


admin.site.register(Articles)

# Register your models here.
