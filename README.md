# mentorec

# 프로젝트 히스토리: 멘토록 (Mentorecord)

## 1. 프로젝트 목표 및 초기 설정 (v1.0)

* **프로젝트명**: 멘토록 (Mentorecord)
* **목표**: 멘토(강사)와 사용자 간의 활동을 기록하고, 강사 프로필 및 커리큘럼을 관리하는 플랫폼
* **기술 스택**: Python, Django, Django Rest Framework, PostgreSQL
* **초기 설정**:
    * Git 저장소 생성 및 GitHub 연동
    * `venv` 가상환경 설정
    * Django 프로젝트 및 초기 앱 구조 생성 (users, instructors, curriculums, logs, ecommerce, ai_assistant)
    * VS Code 환경 설정 (확장 프로그램, settings.json)
    * Django 관리자 페이지 한글화 (`settings.py`: LANGUAGE_CODE, TIME_ZONE)
    * 관리자 페이지 제목 변경 (`urls.py`: admin.site.site_header)

## 2. 사용자(Users) 앱 개발 (v1.1)

* **`models.py`**:
    * `AbstractUser`를 상속받는 커스텀 `User` 모델 생성
    * 역할(Role) 구분을 위한 `role` 필드 추가 (STAFF, INSTRUCTOR, USER)
* **`admin.py`**:
    * 관리자 페이지에 커스텀 `User` 모델이 보이도록 `CustomUserAdmin` 클래스 생성 및 등록
    * `role` 필드 및 강사 프로필 바로가기 링크 추가
* **`serializers.py` & `views.py` & `urls.py`**:
    * **회원가입 API**: `UserRegistrationAPIView` 구현
    * **로그인 API**: `simplejwt`의 `TokenObtainPairView`를 사용하여 JWT 토큰(access, refresh) 발급 기능 구현
    * **내 정보 보기 API**: 인증된 사용자만 접근 가능한 (`IsAuthenticated`) `MyPageAPIView` 구현
    * **비밀번호 변경 API**: 인증된 사용자가 이전 비밀번호를 확인하고 새 비밀번호로 변경하는 `PasswordChangeAPIView` 구현
* **핵심 결정사항**:
    * 다양한 관리자 역할을 위해 Django의 내장 `Group` 및 `Permission` 시스템을 사용하기로 결정. `User` 모델의 `role`은 대분류(스태프, 강사, 일반사용자)에만 사용.
    * API 테스트는 VS Code의 `REST Client` 확장 프로그램을 사용. `test.http` 파일을 통해 진행.

## 3. 강사(Instructors) 앱 개발 (v1.2)

* **`models.py`**:
    * `User` 모델과 1:1로 연결되는 `InstructorProfile` 모델 생성
    * 단순 `TextField`로 시작했던 경력, 학력 등의 항목을 체계적인 관리를 위해 별도의 모델로 분리:
        * `Education` 모델 (학력)
        * `Career` 모델 (경력)
        * `Achievement` 모델 (주요 실적)
        * `Certification` 모델 (자격 및 이수)
        * `Publication` 모델 (논문 및 출간)
    * `Expertise` 모델을 `ManyToManyField` 관계로 분리하여 태그처럼 전문 분야를 관리하도록 개선
    * 파일 첨부를 위해 `Education` 모델과 `Career` 모델에 `FileField` 추가 (`Pillow` 라이브러리 설치 및 `MEDIA` 설정 완료)
* **`admin.py`**:
    * `TabularInline`을 사용하여 강사 프로필 페이지 내에서 학력, 경력 등을 한 번에 관리할 수 있도록 UI 개선
    * `filter_horizontal`을 사용하여 `expertise`를 편리하게 선택하도록 설정
* **`serializers.py` & `views.py` & `urls.py`**:
    * 강사 목록 및 상세 정보를 조회하는 `InstructorProfileViewSet` (읽기 전용) API 구현
* **핵심 결정사항**:
    * `django-simple-history` 라이브러리를 도입하여 `InstructorProfile`의 모든 변경 이력을 자동으로 추적(버전 관리)하도록 결정.

## 4. 커리큘럼(Curriculums) 앱 개발

* *현재 보류. 사용자 관리 기능 보완 후 진행 예정.*