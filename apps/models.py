from django.db import models
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE, BooleanField, \
    DateTimeField


class Category(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title


class Problems(Model):
    class Difficulty(TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium',
        HARD = 'hard', 'Hard'

    title = CharField(max_length=255)
    description = CharField(max_length=500)
    type = CharField(max_length=6, choices=Difficulty.choices)
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.title


class Example(Model):
    output = CharField(max_length=255, blank=True, null=True)
    explanation = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Answer(Model):
    output = CharField(max_length=255)
    example = ForeignKey('apps.Example', CASCADE)


class Submission(Model):
    problems = ForeignKey('apps.Problems', CASCADE)


class InputExample(Model):
    example = ForeignKey('apps.Example', CASCADE)
    variable_name = CharField(max_length=255)
    variable_value = CharField(max_length=255)
