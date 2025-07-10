from django import forms
from .models import Education, Career

class CustomWidthModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 모든 필드의 위젯에 CSS 클래스를 추가합니다.
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'custom-form-width'})

class EducationForm(CustomWidthModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CareerForm(CustomWidthort_description = "사진 미리보기"

# ... (기존 등록 코드는 그대로 유지)
admin.site.register(InstructorProfile, InstructorProfileAdmin)