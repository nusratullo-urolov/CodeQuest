from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Answer, Problems, Task


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


admin.site.register(Task)
