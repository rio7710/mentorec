# instructors/views.py

from rest_framework import viewsets, permissions
from .models import InstructorProfile
from .serializers import InstructorProfileSerializer

class InstructorProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    모든 강사 프로필 목록을 보여주거나, 특정 프로필을 상세 조회합니다.
    """
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
    permission_classes = [permissions.AllowAny] # 누구나 강사 목록을 볼 수 있도록 허용