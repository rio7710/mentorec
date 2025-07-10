from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserSerializer, PasswordChangeSerializer
from .models import User

# 회원가입을 위한 View
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# '내 정보 보기'를 위한 View
class MyPageAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# 비밀번호 변경을 위한 View
class PasswordChangeAPIView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        
        # 1. 이전 비밀번호가 맞는지 확인
        if not user.check_password(serializer.validated_data.get("old_password")):
            return Response({"old_password": ["이전 비밀번호가 일치하지 않습니다."]}, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. 새 비밀번호로 변경 (set_password는 자동 암호화 처리)
        user.set_password(serializer.validated_data.get("new_password"))
        user.save()
        
        return Response({"detail": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)