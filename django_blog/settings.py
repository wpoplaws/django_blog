import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'a9j4*le5)11pw*a+*&rm5h7+r)pq3)31nk=v%kziyg1ahs&$s$'

DEBUG = False

ALLOWED_HOSTS = ['wpoplaws.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrapform',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'taggit',
    'blog',
]

SITE_ID = 1

CKEDITOR_UPLOAD_PATH = "uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_blog.urls'

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

WSGI_APPLICATION = 'django_blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

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

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'post_list'

LOGOUT_REDIRECT_URL = 'login'

RECAPTCHA_PUBLIC_KEY = '6LdaJeYUAAAAAM_9ysufkZMsAsPaYtRGxc_d5edT'

RECAPTCHA_PRIVATE_KEY = "6LdaJeYUAAAAAACnoB1LvH9KLKdnFazxnlG5OfF8"

MAILCHIMP_API_KEY = 'b8d3c395aca99b0fed991736dfcbc68b-us19'
MAILCHIMP_DATA_CENTER = 'us19'
MAILCHIMP_EMAIL_LIST_ID = '2884f1faaf'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
