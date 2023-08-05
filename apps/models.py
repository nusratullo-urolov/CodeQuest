import json

from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE, BooleanField, \
    DateTimeField, SlugField, OneToOneField, JSONField, AutoField, ManyToManyField, TextField
from django.utils.text import slugify

from users.models import User


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
        NONE = 'null', 'None'

    title = CharField(max_length=255, unique=True)
    description = CharField(max_length=500)
    type = CharField(max_length=6, choices=Difficulty.choices)
    category = ForeignKey('apps.Category', CASCADE)
    example = ManyToManyField('apps.Example', null=True, blank=True)
    returning_type = CharField(max_length=10, default=None, choices=DataType.choices)
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)
    view_count = IntegerField(default=0)

    def __str__(self):
        return self.title


class Example(Model):
    variable_value = ManyToManyField('apps.VariableValue')
    output = CharField(max_length=255)
    explanation = CharField(max_length=255, blank=True, null=True)


class VariableValue(Model):
    variable = CharField(max_length=255)
    value = CharField(max_length=255)


class Task(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    complete = BooleanField(default=False)

    def str(self):
        return self.title


class Submission(Model):
    problem = OneToOneField('apps.Problems', CASCADE)
    user = ForeignKey(User, CASCADE)
    answer = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)





