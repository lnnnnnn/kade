"""
Django settings for graph project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3jn+(66o1q^*m#m0my0loaa-u=^tew#&6ou2*c0u$td1i5#d02'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = '*'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'graph.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'graph.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':None,
        'NAME': 'graph',                      # Or path to database file if using sqlite3.
                       # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '32017',
            # 'django.db.backends.dummy',  # 把默认的数据库连接至为None
    }
}



#如果需要mongodb handler session tracking（不明觉厉），注释掉原来的
# SESSION_ENGINE = 'mongoengine.django.sessions'
# SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'
# #SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
#
# #添加这个
# AUTHENTICATION_BACKENDS = ('mongoengine.django.auth.MongoEngineBackend',)





# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#使用session配置-缓存session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置

SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径
SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名
SESSION_COOKIE_SECURE = False  # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存

#CLIENT_URI ='mongodb://lina:111111@localhost:27017/sample'
#CLIENT_URI ='mongodb://localhost:27137/sample'
# from mongoengine import connect # 0.15.3
#connect('sample') # 连接的数据库名称
#connect(DB_NAME,host=DB_HOST,port=DB_PORT,username=DB_USERNAME,password=DB_PASSWORD)


#数据库连接设置


#DB_NAME='cndbpedia'
#DB_HOST='57.300.42.113'
# DB_PORT=32017
# DB_PASSWORD='gd@ata'
# DB_USERNAME='daporter'


#
# DB_NAME='graph_kg'
# DB_HOST='10.141.208.26'
# DB_PORT=27017
# DB_USERNAME='gdmdbuser'
# DB_PASSWORD='6QEUI8dhnq'


# DB_NAME='sample'
# DB_HOST='10.141.209.145'
# DB_PORT=32017
# DB_USERNAME=''
# DB_PASSWORD=''
#
DB_NAME='graph'
DB_HOST='localhost'
DB_PORT=32017
DB_USERNAME='lina'
DB_PASSWORD='111111'


CLIENT_URI = 'mongodb://' +  DB_HOST + ':' + str(DB_PORT) + '/' + DB_NAME

# if DB_USERNAME=='' and DB_PASSWORD=='':
#
#
# else:
#     #uri方式连接数据库需要将@替换为40%
#     DB_PASSWORD=DB_PASSWORD.replace('@','%40')
#     CLIENT_URI ='mongodb://'+DB_USERNAME+':'+DB_PASSWORD+'@'+DB_HOST+':'+str(DB_PORT)+'/'+DB_NAME
#
#
