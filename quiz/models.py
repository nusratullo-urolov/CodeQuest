from django.db.models import Model, CharField, ForeignKey, CASCADE, TextChoices
from django.forms import BooleanField


class QuestionCategory(Model):
    name = CharField(max_length=200, null=True)


# Create your here.
class Question(Model):
    class Difficulty(TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium',
        HARD = 'hard', 'Hard'

    question = CharField(max_length=200, null=True)
    op1 = CharField(max_length=200, null=True)
    op2 = CharField(max_length=200, null=True)
    op3 = CharField(max_length=200, null=True)
    op4 = CharField(max_length=200, null=True)
    answer = CharField(max_length=200, null=True)
    category = ForeignKey(QuestionCategory, CASCADE)

    def __str__(self):
        return self.question
