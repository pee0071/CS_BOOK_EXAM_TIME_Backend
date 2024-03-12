from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet , StudentEnrolledViewSet

router = DefaultRouter()
router.register(r'subject', SubjectViewSet) 
router.register(r'studentEnrolled', StudentEnrolledViewSet)
# router.register(r'teacherEnrolled', TeacherEnrolledViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
