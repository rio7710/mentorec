from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import User

class CustomUserAdmin(UserAdmin):
    # 'role'과 '프로필 링크'를 개인 정보 섹션 바로 아래에 배치
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("개인 정보", {"fields": ("first_name", "last_name", "email")}),
        # --- '추가 정보' 섹션을 위로 올리고, 링크 필드를 추가합니다. ---
        ("추가 정보", {"fields": ("role", "instructor_profile_link")}),
        # ----------------------------------------------------
        (
            "권한",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("주요 날짜", {"fields": ("last_login", "date_joined")}),
    )
    # 사용자 목록에 role 필드 표시
    list_display = ('username', 'email', 'is_staff', 'role')
    # 링크 필드는 읽기 전용으로 설정
    readonly_fields = ('instructor_profile_link',)

    # 강사 프로필로 바로 가는 링크를 생성하는 함수
    def instructor_profile_link(self, obj):
        if obj.role == User.Role.INSTRUCTOR:
            # 강사 프로필 객체가 존재하면 변경 페이지로, 없으면 추가 페이지로 링크
            try:
                profile_id = obj.instructorprofile.user_id
                url = reverse('admin:instructors_instructorprofile_change', args=[profile_id])
                return format_html('<a href="{}">✅ 강사 프로필 바로가기</a>', url)
            except AttributeError:
                url = reverse('admin:instructors_instructorprofile_add') + f'?user={obj.id}'
                return format_html('<a href="{}">➕ 강사 프로필 생성하기</a>', url)
        return "- (강사가 아님) -"
    
    # 함수 결과의 컬럼 제목 설정
    instructor_profile_link.short_description = '프로필 링크'


# User 모델을 우리가 만든 CustomUserAdmin으로 등록합니다.
admin.site.register(User, CustomUserAdmin)