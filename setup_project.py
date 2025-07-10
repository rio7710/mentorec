import os
import subprocess

# --- 설정 ---
PROJECT_NAME = "mentorecord"
APPS = [
    "users",
    "instructors",
    "curriculums",
    "logs",
    "ecommerce",
    "ai_assistant",
]
# ------------

def run_command(command):
    """주어진 명령어를 실행합니다."""
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"✅  Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"❌  Error executing command: {command}\n{e}")
        exit()

def create_django_structure():
    """장고 프로젝트와 앱 구조를 생성합니다."""
    print("--- 1. 가상환경 생성 및 라이브러리 설치 ---")
    # .venv 폴더가 없다면 가상환경 생성
    if not os.path.exists('.venv'):
        run_command(f"python -m venv .venv")
    else:
        print("✅  가상환경(.venv)이 이미 존재합니다.")

    # OS에 맞는 pip 경로 설정
    pip_executable = ".\\.venv\\Scripts\\pip" if os.name == 'nt' else "./.venv/bin/pip"
    run_command(f"{pip_executable} install django djangorestframework djangorestframework-simplejwt psycopg2-binary reportlab python-docx")

    print(f"\n--- 2. '{PROJECT_NAME}' 프로젝트 및 앱 생성 ---")
    # manage.py 파일이 없다면 프로젝트 생성
    if not os.path.exists('manage.py'):
        django_admin = ".\\.venv\\Scripts\\django-admin" if os.name == 'nt' else "./.venv/bin/django-admin"
        run_command(f"{django_admin} startproject {PROJECT_NAME} .")
    else:
        print(f"✅  '{PROJECT_NAME}' 프로젝트가 이미 존재합니다.")
    
    manage_py = f"python manage.py"
    for app in APPS:
        # 해당 앱 폴더가 없다면 앱 생성
        if not os.path.exists(app):
            run_command(f"{manage_py} startapp {app}")
            # 각 앱 내부에 추가 파일 생성
            open(os.path.join(app, 'serializers.py'), 'a').close()
            open(os.path.join(app, 'permissions.py'), 'a').close()
            print(f"    - '{app}' 앱에 'serializers.py', 'permissions.py' 추가 완료")
        else:
            print(f"    - '{app}' 앱이 이미 존재합니다.")


    print("\n🎉 모든 프로젝트 구조 생성이 완료되었습니다!")
    print("개발을 시작할 준비가 되었습니다.")


if __name__ == "__main__":
    create_django_structure()