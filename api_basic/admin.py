from django.contrib import admin
from .models import Articles, Love


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ()


admin.site.register(Articles)
admin.site.register(Love)

# Register your models here.
