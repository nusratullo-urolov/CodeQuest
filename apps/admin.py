from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import Category, Example, Answer, Problems, InputExample


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Problems)
class CategoryModelAdmin(ModelAdmin):
    pass


class InputExampleModelAdmin(StackedInline):
    model = InputExample
    max_num = 3


@admin.register(Example)
class CategoryModelAdmin(ModelAdmin):
    inlines = [InputExampleModelAdmin]


@admin.register(Answer)
class CategoryModelAdmin(ModelAdmin):
    pass
