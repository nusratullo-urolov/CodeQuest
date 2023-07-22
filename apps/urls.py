from django.urls import path, include

from apps.views import home, categories, problems, problem

urlpatterns = [
    # path('solution/',solutions,name='solution'),
    path('categories/', categories, name='categories'),
    path('problems/<int:id>',problems,name='problems'),
    path('problem/<int:id>',problem,name='problem'),
    path('', home, name='home')
]
