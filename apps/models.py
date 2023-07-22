import json

from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE, BooleanField, \
    DateTimeField, SlugField, OneToOneField, JSONField
from django.utils.text import slugify





class Category(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title


class Problems(Model):
    class Difficulty(TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium',
        HARD = 'hard', 'Hard'

    title = CharField(max_length=255, unique=True)
    description = CharField(max_length=500)
    type = CharField(max_length=6, choices=Difficulty.choices)
    category = ForeignKey('apps.Category', CASCADE)
    input = JSONField()
    output = CharField(max_length=255)
    explanation = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    # def get_example(self):
        # for k,v in Problems.objects.filter()
            # return


class Answer(Model):
    output = CharField(max_length=255)
    problems = OneToOneField('apps.Problems', CASCADE)


class Submission(Model):
    problems = OneToOneField('apps.Problems', CASCADE)
