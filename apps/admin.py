from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Example, Answer, Problems


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Problems)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Example)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Answer)
class CategoryModelAdmin(ModelAdmin):
    pass
