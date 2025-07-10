from django.apps import AppConfig

class InstructorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instructors'
    verbose_name = '강사 관리' # 이 줄을 추가 또는 수정합니다.