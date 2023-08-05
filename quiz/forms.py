from django.forms import ModelForm

from quiz.models import *
from django import forms


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
