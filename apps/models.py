from django.db import models
from django.db.models import Model, TextChoices, CharField, IntegerField, ForeignKey, CASCADE, BooleanField, \
    DateTimeField, SlugField, OneToOneField
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
    # slug = SlugField(unique=True)
    type = CharField(max_length=6, choices=Difficulty.choices)
    category = ForeignKey('apps.Category', CASCADE)

    # def save(self,*args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         while Problems.objects.filter(slug=self.slug).exists():
    #             self.slug = f'{self.slug}-1'
    #     return super().save(*args,**kwargs)

    def __str__(self):
        return self.title


class Example(Model):
    output = CharField(max_length=255, blank=True, null=True)
    explanation = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    problems = OneToOneField('apps.Problems', CASCADE)


class Answer(Model):
    output = CharField(max_length=255)
    problems = OneToOneField('apps.Problems', CASCADE)


class Submission(Model):
    problems = OneToOneField('apps.Problems', CASCADE)


class InputExample(Model):
    example = OneToOneField('apps.Example', CASCADE)
    variable_name = CharField(max_length=255)
    variable_value = CharField(max_length=255)
