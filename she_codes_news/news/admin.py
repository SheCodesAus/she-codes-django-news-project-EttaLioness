from django.contrib import admin

# Register your models here.

from .models import NewsStory, Category

admin.site.register(NewsStory)
admin.site.register(Category)
