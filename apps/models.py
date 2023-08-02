import json

from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE, BooleanField, \
    DateTimeField, SlugField, OneToOneField, JSONField, AutoField
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

    class DataType(TextChoices):
        INT = 'int', 'Int',
        STR = 'str', 'Str',
        LIST = 'list', 'List',
        BOOL = 'bool', 'Bool',
        FLOAT = 'float', 'Float',
        DICT = 'dict', 'Dict',
        SET = 'set', 'Set',

    title = CharField(max_length=255, unique=True)
    description = CharField(max_length=500)
    type = CharField(max_length=6, choices=Difficulty.choices)
    category = ForeignKey('apps.Category', CASCADE)
    input = JSONField()
    output = CharField(max_length=255)
    explanation = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    data_type = CharField(max_length=15, choices=DataType.choices, blank=True, null=True)

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



class Task(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    complete = BooleanField(default=False)

    def str(self):
        return self.title