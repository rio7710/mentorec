from django.contrib import admin
from django.utils.html import format_html
from .models import (
    InstructorProfile, Education, Career, 
    Achievement, Certification, Publication, Expertise
)

# --- 인라인 섹션 ---
# 각 모델을 강사 프로필 페이지 안에서 함께 편집하기 위한 설정입니다.

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1 # 기본으로 보여줄 추가 입력 폼의 수

class CareerInline(admin.TabularInline):
    model = Career
    extra = 1

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1

# --- 강사 프로필 관리자 페이지 커스터마이징 ---

class InstructorProfileAdmin(admin.ModelAdmin):
    # 위에서 정의한 인라인들을 등록합니다.
    inlines = [
        EducationInline, CareerInline, AchievementInline, 
        CertificationInline, PublicationInline
    ]
    # ManyToManyField인 'expertise'를 편리하게 선택할 수 있도록 필터 виджет을 추가합니다.
    filter_horizontal = ('expertise',)
    
    # 강사 프로필 목록에 표시할 필드를 지정합니다.
    list_display = ('__str__', 'get_profile_image_preview')
    
    # 상세 페이지에서 사진 미리보기를 보여주기 위해 읽기 전용 필드로 등록합니다.
    readonly_fields = ('get_profile_image_preview',)

    # 프로필 사진 미리보기를 생성하는 함수입니다.
    def get_profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html(f'<img src="{obj.profile_image.url}" style="height: 50px; width: auto;" />')
        return "이미지 없음"
    # 관리자 페이지에 표시될 컬럼의 제목을 설정합니다.
    get_profile_image_preview.short_description = "사진 미리보기"


# --- 최종 등록 ---

# Expertise 모델을 먼저 관리자에 등록합니다.
admin.site.register(Expertise)

# 기존에 등록된 InstructorProfile이 있다면 해제하고,
# 새로 만든 커스텀 Admin 클래스로 다시 등록합니다.
try:
    admin.site.unregister(InstructorProfile)
except admin.sites.NotRegistered:
    pass
admin.site.register(InstructorProfile, InstructorProfileAdmin)