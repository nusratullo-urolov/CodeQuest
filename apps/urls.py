from django.conf.urls.static import static
from django.urls import path

from apps.views import home, categories, problems, problem, submission, homee, add, update, delete, about
from root import settings

urlpatterns = [
    path('todo', homee, name='todo'),
    path('add', add, name='add'),
    path('update/<int:todo_id>/', update, name='update'),
    path('delete/<int:todo_id>/', delete, name='delete'),

    path('about/', about, name='about'),
    # path('solution/',solutions,name='solution'),
    path('categories/', categories, name='categories'),
    path('problems/<int:id>', problems, name='problems'),
    path('problem/<int:id>', problem, name='problem'),
    path('', home, name='home'),
    path('problem/<int:id>/submission', submission, name='submission'),

]
