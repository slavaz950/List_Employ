
from pathlib import Path
import os,sys



# Основной каталог проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Было изначально



# BASE_DIR = Path(__file__).resolve().parent.parent # ------------------------
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = 'C:\django\List_Employ'
# BASE_DIR = os.path.dirname('C:\django\List_Employ')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gbcv_hut0q^==1vsvk38u0n0slc4+xqk!q7zoxm_^q=m8yfo)a'

# SECURITY WARNING: don't run with debug turned on in production!
# Режим отладки (отключить по завершению разработки)
DEBUG = True

ALLOWED_HOSTS = [
    
    '127.0.0.1',
    'localhost',
    'example.com',
    'www.yourdomain.com'
]
    
print(BASE_DIR)

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',  # Перенаправления Redirect
    'ListEmp',
    # 'bootstrap5',
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
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
    # 'ListEmp.middleware.disableCSRF', # Отключение проверки CSRF (чтоб избежать ошибок)
]

CORS_ORIGIN_ALLOW_ALL = True



ROOT_URLCONF = 'List_Employ.urls'

TEMPLATES = [  #  ЕСЛИ ВСЁ РАБОТАЕТ НАВЕСТИ ПОРЯДОК
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        
       #  'DIRS': [os.path.join(BASE_DIR,'List_Employ', 'ListEmp/templates/ListEmp')],
        
        
        # 'List_Employ/ListEmp/templates/'                          os.path.join(BASE_DIR, 'ListEmp/templates/ListEmp')
# 'templates'
# 'ListEmp/templates/'                               'ListEmp',    'List_Employ'





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
CSRF_COOKIE_DOMAIN = '127.0.0.1'


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

# НАСТРОЙКА КАТАЛОГА ХРАНЕНИЯ СТАТИЧНЫХ ФАЙЛОВ
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
   #  BASE_DIR / 'List_Employ' / 'static', #type: str      # Полный путь к папке static 
    os.path.join(BASE_DIR, 'List_Employ', 'static'),  # Правильный способ
    
]

# STATIC_ROOT = BASE_DIR / 'staticfiles'  # Для collectstatic (production)  --------------------------------------

# STATIC_ROOT = os.path.join(str(BASE_DIR), 'staticfiles')   #type: str   # Одна строка!

STATIC_URL = '/static/'



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


'''

SITE_ID

Значение является идентификатором записи из таблицы БД "django_site"

Django и зависимые приложения используют модель Site с полями domain и name, 
которую предоставляет фреймворк django.contrib.sites. SITE_ID указывает идентификатор 
объекта Site, связанного с этим файлом настроек. 

Если настройка не указана, функция get_current_site() попытается получить текущий сайт, 
сравнив его домен с именем хоста из метода request.get_host()

По умолчанию django.contrib.sites создаёт объект с ID=1. Если в проекте несколько 
сайтов или их пересоздавали, ID может отличаться. 

'''
SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_RENDER_CLASSES': [
        'rest_framework.renderers.JSONRenderer', # Разрешаем JSONRenderer (Если используем JSON)
        'rest_framework.renderers.TemplateHTMLRenderer',  # Разрешаем TemplateHTMLRenderer (Если нужен HTML)
        'rest_framework.renderers.BrowsableAPIRenderer',  # Разрешаем рендер DRF (по умолчанию. Веб-интерфейс для взаимодействия с API непосредственно в браузере)
    ]
    
}









# print(SITE_ID)