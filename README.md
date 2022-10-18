# python-study

1. 가상환경 생성
python -m venv [name]
 - -m = module을 실행한다는 뜻

2. 가상환경 실행
./[name]/Scripts/activate

3. 장고 설치
python -m pip install Django
 - 설치 확인 
 python -m django --version

4. 장고 프로젝트 생성
django-admin startproject [project]

5. 장고 프로젝트 실행
python manage.py runserver

6. 장고 앱 생성
python manage.py startapp [app]

7. 마이그레이션 반영
python manage.py migrate
- migrate 명령은 INSTALLED_APPS 의 설정을 탐색하여, project/settings.py 의 데이터베이스 설정과 app 과 함께 제공되는 database migrations(나중에 다루겠습니다) 에 따라, 필요한 데이터베이스 테이블을 생성합니다. 

8. 모델 생성
app/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

9. 모델 활성화 및 마이그레이션 파일 추가
 - 설정값 추가 
    INSTALLED_APPS = [
        'app.apps.appConfig',
        ...
    ]
python manage.py makemigrations [app]

10. SQL 확인
python manage.py sqlmigrate [app] 0001

11. 마이그레이션 반영
python manage.py migrate

12. 관리자 생성
python manage.py createsuperuser

 - rohyunge
 - soaql1102!


13. DRF 설치
pip install djangorestframework
    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]

14. DRF swagger 설치
pip install drf-yasg
    INSTALLED_APPS = [
        'drf_yasg',
    ]

15. 