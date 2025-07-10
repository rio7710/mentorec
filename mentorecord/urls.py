"""
URL configuration for mentorecord project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# mentorecord/urls.py
from django.contrib import admin
from django.urls import path, include
# 아래 두 줄을 새로 import 합니다.
from django.conf import settings
from django.conf.urls.static import static

# --- 관리자 페이지 제목 변경 ---
admin.site.site_header = "MERE 서비스 관리"  # 메인 헤더
admin.site.site_title = "MERE 서비스 포털"     # 브라우저 탭 제목
admin.site.index_title = "MERE 서비스 관리" # 메인 페이지 제목
# ---------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/instructors/', include('instructors.urls')),
]

# 개발 환경에서 미디어 파일을 서빙하기 위한 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)