from django.db import models
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE


class Category(Model):
    title = CharField(max_length=255)


class Problems(Model):
    class Difficulty(TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium',
        HARD = 'hard', 'Hard'

    title = CharField(max_length=255)
    description = CharField(max_length=500)
    type = CharField(max_length=6, choices=Difficulty.choices)
    acceptance = IntegerField()
    category = ForeignKey('apps.Category', CASCADE)


class Example(Model):
    input = CharField(max_length=255)
    output = CharField(max_length=255, null=True)
    explanation = CharField(max_length=255, null=True)
    target = CharField(max_length=255, null=True)


class Answer(Model):
    output = CharField(max_length=255)
    example = ForeignKey('apps.Example', CASCADE)
    runtime = CharField(max_length=25)
