from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords

class Expertise(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="전문 분야명")

    class Meta:
        verbose_name = "전문 분야"
        verbose_name_plural = "전문 분야(들)"

    def __str__(self):
        return self.name

class InstructorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="사용자"
    )
    # --- 프로필 이미지 필드 추가 ---
    profile_image = models.ImageField(upload_to='instructor_profiles/', null=True, blank=True, verbose_name="프로필 사진")
    # --- 강사 소개 필드 추가 ---
    bio = models.TextField(blank=True, verbose_name="강사 소개")
    expertise = models.ManyToManyField(Expertise, blank=True, verbose_name="전문 분야")
    years_of_experience = models.PositiveIntegerField(default=0, verbose_name="경력 (년수)")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="생년월일")
    affiliation = models.CharField(max_length=255, blank=True, verbose_name="소속")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="전화번호")
    
    history = HistoricalRecords()

    class Meta:
        verbose_name = "강사 프로필"
        verbose_name_plural = "강사 프로필(들)"

    def __str__(self):
        return f"{self.user.username} - Instructor Profile"

class Education(models.Model):
    instructor_profile = models.ForeignKey(InstructorProfile, related_name='education_history', on_delete=models.CASCADE, verbose_name="강사 프로필")
    school_name = models.CharField(max_length=255, verbose_name="학교명")
    major = models.CharField(max_length=255, verbose_name="전공")
    degree = models.CharField(max_length=100, verbose_name="학위")
    start_date = models.DateField(verbose_name="입학 연월")
    end_date = models.DateField(null=True, blank=True, verbose_name="졸업 연월")
    # --- 이미지 필드 추가 ---
    degree_documen = models.FileField(upload_to='education_degrees/', null=True, blank=True, verbose_name="학위 증명서")


    class Meta:
        verbose_name = "학력"
        verbose_name_plural = "학력(들)"

    def __str__(self):
        return f"{self.school_name} - {self.degree}"

class Career(models.Model):
    instructor_profile = models.ForeignKey(InstructorProfile, related_name='career_history', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, verbose_name="회사/기관명")
    position = models.CharField(max_length=255, verbose_name="직책")
    description = models.TextField(blank=True, verbose_name="담당업무")
    start_date = models.DateField(verbose_name="시작일")
    end_date = models.DateField(null=True, blank=True, verbose_name="종료일")
    
# --- 파일 필드 추가 ---
    proof_document = models.FileField(upload_to='career_proofs/', blank=True, null=True, verbose_name="경력 증빙 자료")

    class Meta:
        verbose_name = "경력"
        verbose_name_plural = "경력(들)"

    def __str__(self):
        return f"{self.company_name} - {self.position}"

class Achievement(models.Model):
    instructor_profile = models.ForeignKey(InstructorProfile, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="실적/프로젝트명")
    description = models.TextField(blank=True, verbose_name="상세 내용")
    achieved_date = models.DateField(null=True, blank=True, verbose_name="달성일")

    class Meta:
        verbose_name = "주요 실적"
        verbose_name_plural = "주요 실적(들)"

    def __str__(self):
        return self.title

class Certification(models.Model):
    instructor_profile = models.ForeignKey(InstructorProfile, related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="자격증명")
    issuer = models.CharField(max_length=255, verbose_name="발급기관")
    issued_date = models.DateField(null=True, blank=True, verbose_name="취득일")

    class Meta:
        verbose_name = "자격 및 이수"
        verbose_name_plural = "자격 및 이수(들)"

    def __str__(self):
        return self.name

class Publication(models.Model):
    instructor_profile = models.ForeignKey(InstructorProfile, related_name='publications', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="논문/출간물 제목")
    publisher = models.CharField(max_length=255, verbose_name="학회/출판사")
    published_date = models.DateField(null=True, blank=True, verbose_name="발행일")

    class Meta:
        verbose_name = "논문 및 출간"
        verbose_name_plural = "논문 및 출간(들)"

    def __str__(self):
        return self.title