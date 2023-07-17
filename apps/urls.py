from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProblemsView

router = DefaultRouter()
router.register('problems', ProblemsView, 'problems')
urlpatterns = [
    path('', include(router.urls))
]
