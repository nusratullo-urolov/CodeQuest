from django.urls import path, include

from apps.views import home, categories, problems, problem, about

urlpatterns = [
    path('about/', about, name='about'),
    # path('solution/',solutions,name='solution'),
    path('categories/', categories, name='categories'),
    path('problems/<int:id>', problems, name='problems'),
    path('problem/<str:title>', problem, name='problem'),
    path('', home, name='home')
]
