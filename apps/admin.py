from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import Category, Answer, Problems


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Problems)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Answer)
class CategoryModelAdmin(ModelAdmin):
    pass
