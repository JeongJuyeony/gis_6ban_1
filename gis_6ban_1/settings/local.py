from .base import *


env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'), encoding='utf-8')  # 불러들이기
# 운영체제의 경로탐색에서 BASE_DIR과 env 파일을 join 즉, 최상위 폴더 gis_6ban_1에 있는 env 파일을 oepn

while True:
    line = local_env.readline()  # 라인 한줄씩 읽기
    if not line:  # 라인이 없다면 break
        break
    line = line.replace('\n', '')
    start = line.find('=')  # =의 위치를 판단하고 인덱스 알려준 후 start에 저장
    key = line[:start]  # 시크릿 키에서 =을 기준으로 왼쪽을 key 오른쪽을 value로 판단
    value = line[start + 1:]
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
