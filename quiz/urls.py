from django.contrib import admin
from django.urls import path
from quiz.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('quiz-home', quiz_home, name='quiz_home'),
    path('add-question/', add_question, name='addQuestion'),
    path('quiz_category/', quiz_categories, name='quiz_category'),
    path('quiz_home/<int:id>', quiz_home, name='quiz_home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
