from django.contrib.auth.models import AbstractUser
from django.db import models

# --- Affiliation 모델 새로 추가 ---
class Affiliation(models.Model):
    class Type(models.TextChoices):
        SCHOOL = "SCHOOL", "학교"
        COMPANY = "COMPANY", "회사"
        ETC = "ETC", "기타"

    name = models.CharField(max_length=255, verbose_name="소속명")
    type = models.CharField(
        max_length=50,
        choices=Type.choices,
        default=Type.COMPANY,
        verbose_name="소속 종류"
    )

    class Meta:
        verbose_name = "소속"
        verbose_name_plural = "소속(들)"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
# ------------------------------------

class User(AbstractUser):
    class Role(models.TextChoices):
        STAFF = "STAFF", "스태프"
        INSTRUCTOR = "INSTRUCTOR", "강사"
        USER = "USER", "일반사용자"

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.USER,
    )
    # --- affiliations 필드 추가 ---
    affiliations = models.ManyToManyField(
        Affiliation,
        blank=True,
        verbose_name="소속"
    )
    # -----------------------------

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.STAFF
        super().save(*args, **kwargs)