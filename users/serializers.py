from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

# 회원가입을 위한 Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# 사용자 정보 조회를 위한 Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']

# 비밀번호 변경을 위한 Serializer
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate_new_password(self, value):
        # Django의 기본 비밀번호 정책(길이, 복잡성 등)을 통과하는지 검증합니다.
        validate_password(value)
        return value