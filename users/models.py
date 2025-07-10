# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    class Role(models.TextChoices):
        # 관리자 그룹을 'STAFF'로 통칭
        STAFF = "STAFF", "스태프"
        INSTRUCTOR = "INSTRUCTOR", "강사"
        USER = "USER", "일반사용자"

    # 기본 역할은 '일반사용자'
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.USER,
    )

    # 슈퍼유저는 항상 STAFF이자 모든 권한을 가짐
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.STAFF
        super().save(*args, **kwargs)