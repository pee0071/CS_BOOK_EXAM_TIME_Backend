from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotepadViewSet

router = DefaultRouter()
router.register(r'notepad', NotepadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
