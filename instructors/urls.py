# instructors/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorProfileViewSet

# 라우터를 생성합니다.
router = DefaultRouter()
# InstructorProfileViewSet을 'profiles'라는 이름으로 라우터에 등록합니다.
router.register('', InstructorProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]