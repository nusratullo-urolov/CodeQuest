from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import Category, Problems, Example, VariableValue


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Problems)
class CategoryModelAdmin(ModelAdmin):
    pass





@admin.register(Example)
class ExampleModelAdmin(ModelAdmin):
    pass

@admin.register(VariableValue)
class VariableValueModelAdmin(ModelAdmin):
    pass
