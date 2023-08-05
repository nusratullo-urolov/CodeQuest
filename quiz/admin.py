from django.contrib import admin

from quiz.models import Question, QuestionCategory


class QuestionInline(admin.TabularInline):
    model = Question


#
#
class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]
    list_display = ['title', ]


admin.site.register(Question)
admin.site.register(QuestionCategory)