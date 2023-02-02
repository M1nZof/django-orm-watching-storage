import os
from environs import Env

env = Env()
env.read_env()  
db_host = env.str('DB_HOST')
db_port = env.str('DB_PORT')
db_name = env.str('DB_NAME')
db_user = env.str('DB_USER')
db_password = env.str('DB_PASSWORD')
secret_key = env.str('SECRET_KEY', '123')
debug_mode = env.bool('DEBUG', True)
allowed_hosts = env.list('ALLOWED_HOSTS', '*')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug_mode

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = allowed_hosts


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
