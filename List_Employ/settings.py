
from pathlib import Path
import os,sys

# Основной каталог проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gbcv_hut0q^==1vsvk38u0n0slc4+xqk!q7zoxm_^q=m8yfo)a'

# SECURITY WARNING: don't run with debug turned on in production!
# Режим отладки (отключить по завершению разработки)
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ListEmp',
    'bootstrap5',
    'psycopg2',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'ListEmp.middleware.disableCSRF', # Отключение проверки CSRF (чтоб избежать ошибок)
]

CORS_ORIGIN_ALLOW_ALL = True



ROOT_URLCONF = 'List_Employ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['List_Employ/ListEmp/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'List_Employ.wsgi.application'

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000/']


# Настройки подключения к БД   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Драйвер (адаптер) 
        'NAME': 'ListEmpDB', # Имя Базы Данных
        'USER': 'postgres', # Пользователь БД 
        'PASSWORD': 'Cen78Ter19', # Пароль пользователя БД
        'HOST': 'localhost',  # Местоположение БД
        'PORT': '5432', 
     }
    
    
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# Настройка каталога хранения статичных файлов
STATIC_URL = 'static/'
STATICFILES_DIR = os.path.join(BASE_DIR, 'ListEmp/static/')  # Каталог для статичных файлов

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
