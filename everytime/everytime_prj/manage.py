#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django

# 필수 카테고리 정의
REQUIRED_CATEGORIES = [
    {'name': '비밀게시판', 'slug': 'secret'},
    {'name': '자유게시판', 'slug': 'free'},
    {'name': '새내기게시판', 'slug': 'freshman'},
]


def main():
    """Run administrative tasks and ensure essential data exists."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'everytime.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        # 1. Django 환경 설정 로드
        django.setup()
        
        # 2. Category 모델 임포트 (앱 이름에 맞게 수정 필요)
        # 예시: 'posts' 앱에 Category 모델이 있다고 가정
        from posts.models import Category 
        
        # 3. 필수 카테고리 확인 및 생성
        for cat_data in REQUIRED_CATEGORIES:
            # get_or_create를 사용하여 해당 slug의 카테고리가 없으면 새로 생성
            Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
        
        # print("필수 카테고리 데이터베이스 초기화 완료.") # 필요 시 주석 해제

    except Exception as e:
        # DB 연결이 안 되었거나(migrate 전) 모델이 없는 경우 등
        # print(f"경고: 데이터 초기화 중 오류 발생 ({e}). 명령 실행을 계속합니다.")
        pass # 오류 발생 시 무시하고 다음 단계로 진행

    # 실제 관리 명령 실행
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()