import os
from environs import Env

env = Env()
env.read_env()  
db_host = env.str('DB_HOST')
db_password = env.str('DB_PASSWORD')
secret_key = env.str('SECRET_KEY')
debug_mode = env.bool('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': f'{db_host}',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': f'{db_password}',
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = f'{secret_key}'

DEBUG = debug_mode

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
