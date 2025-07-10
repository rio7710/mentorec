from django.contrib import admin
from .models import (
    InstructorProfile, Education, Career, 
    Achievement, Certification, Publication, Expertise
)

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

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

class InstructorProfileAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline, CareerInline, AchievementInline, 
        CertificationInline, PublicationInline
    ]
    filter_horizontal = ('expertise',)

# Expertise 모델을 먼저 등록합니다.
admin.site.register(Expertise)

# InstructorProfile을 등록합니다. (이미 등록되었다면 이전에 등록된 것을 자동으로 관리합니다)
# 혹시 모르니 기존 등록을 해제하는 코드를 포함할 수 있지만, 일반적으로는 필요 없습니다.
try:
    admin.site.unregister(InstructorProfile)
except admin.sites.NotRegistered:
    pass
admin.site.register(InstructorProfile, InstructorProfileAdmin)