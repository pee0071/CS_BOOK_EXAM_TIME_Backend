from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    path("signup/", api.signup, name="signup"),
    # login จะเรียก Method ที่ Return Token โดย Method เป็นของ  Django
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("userInfo/", api.userInfo, name='userInfo'),
]
