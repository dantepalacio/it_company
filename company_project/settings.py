from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-k%3-e38%&4_jz@olj0qkzdjtujg1m06ri=ffc_o-m%-ew13doo'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'crispy_forms',

    'company_app'
]



MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]





ROOT_URLCONF = 'company_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'company_app.context_processor.contact',
            ],
        },
    },
]

WSGI_APPLICATION = 'company_project.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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




TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('kk', _('Қазақша')),
    ('en', _('English')),
    ('ru', _('Русский')),
)

LANGUAGE_CODE = 'kk'

# DATA_UPLOAD_MAX_MEMORY_SIZE = 

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aliktest3@gmail.com'
EMAIL_HOST_PASSWORD = 'oimixghgsetizbqj'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587



JAZZMIN_SETTINGS = {
    "site_title": _("Administration Panel"),
    "site_header": _("Admin panel"),
    "site_brand": _("Admin panel"),
    "welcome_sign": _("Welcome"),
    # "copyright": "Права на футер",
    "site_logo": None,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

     "topmenu_links": [
         {"name": "Электрондық поштаны қолдау қызметі",  "url": "/answer/", "permissions": ["auth.view_user"]},
         
     ],

    # Side Menu
    "navigation_expanded": True,

}

JAZZMIN_UI_TWEAKS = {
    "theme": "Cosmo",

    "custom_css": None,
    "custom_js": None,

}