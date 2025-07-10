from django.urls import path
from .views import (
    UserRegistrationAPIView, 
    MyPageAPIView,
    PasswordChangeAPIView,
    UserDeactivationAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', MyPageAPIView.as_view(), name='user-me'),
    path('password/change/', PasswordChangeAPIView.as_view(), name='password-change'),
    path('deactivate/', UserDeactivationAPIView.as_view(), name='user-deactivate'),
]