from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("account.urls")),
    path("", include("subject.urls")),
    path("", include("book_exam.urls")),
]
