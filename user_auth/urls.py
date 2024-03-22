from django.urls import path
from .views import PasswordResetRequestAPIView, PasswordResetValidateAPIView, RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('register/',RegisterUserAPIView.as_view(), name='register_new_user'),
    path('login/', TokenObtainPairView.as_view(), name='login_token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_token_refresh'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetValidateAPIView.as_view(), name='password_reset_confirm'),
]