from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotepadViewSet,ExamDetailViewSet

router = DefaultRouter()
router.register(r'notepad', NotepadViewSet)
router.register(r'examdetail', ExamDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
