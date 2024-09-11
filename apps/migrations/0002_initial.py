# Generated by Django 4.2.3 on 2023-08-05 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problems',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.category'),
        ),
        migrations.AddField(
            model_name='problems',
            name='example',
            field=models.ManyToManyField(blank=True, null=True, to='apps.example'),
        ),
        migrations.AddField(
            model_name='example',
            name='variable_value',
            field=models.ManyToManyField(to='apps.variablevalue'),
        ),
    ]