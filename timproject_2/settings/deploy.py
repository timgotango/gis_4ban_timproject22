from .base import *



env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))
# 파일 오픈 : 운영체제 os 상 경로(path) 에서 BASE_DIR과 .env를 join(합쳐준다)

while True:
    line = local_env.readline() # 한줄 한줄씩 읽어서 line 변수에 넣어주고,
    if not line: # 파일의 끝에 도달하면 break
        break
    line = line.replace('\n', '') # 줄바꿈 문자열을 공백으로 치환
    start = line.find('=') # SECRET_KEY = 이 있기 때문에 = 의 위치 찾는 find() 함수 사용
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value # 딕셔너리에 key, value 삽입


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY'] # 나중에 dictionary 만들 것이다.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}