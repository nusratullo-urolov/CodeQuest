from django.urls import path, include

from apps.views import home, categories, problems, solutions

urlpatterns = [
    path('solution/',solutions,name='solution'),
    path('categories/', categories, name='categories'),
    path('problems/<int:id>',problems,name='problems'),
    path('', home, name='home')
]
