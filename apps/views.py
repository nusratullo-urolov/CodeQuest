from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.models import Problems
from apps.serializers import ProblemsModelSerializer


class ProblemsView(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsModelSerializer