from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.postgres.fields import ArrayField

from apps.models import Category, Answer, Problems


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Problems)
class CategoryModelAdmin(ModelAdmin):
    pass
    # formfield_overrides = {
    #     ArrayField: {'widget': admin.widgets.AdminTextInputWidget},
    # }


@admin.register(Answer)
class CategoryModelAdmin(ModelAdmin):
    pass
