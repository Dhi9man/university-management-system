# university_mgmt/settings.py

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "p5@_%l*2=(f-=iuc-$=s19h%beuc2**r_%szj8u+hcu3a00ysc"

from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environment variables
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

from pathlib import Path
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split(",") if env("ALLOWED_HOSTS", default="") else []


INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"rest_framework",
"accounts",
"academics",
]


MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "university_mgmt.urls"


TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "templates"],
"APP_DIRS": True,
"OPTIONS": {
"context_processors": [
"django.template.context_processors.debug",
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
],
},
},
]


WSGI_APPLICATION = "university_mgmt.wsgi.application"
ASGI_APPLICATION = "university_mgmt.asgi.application"


DATABASES = {
"default": {
"ENGINE": "django.db.backends.sqlite3",
"NAME": BASE_DIR / env("DB_NAME", default="db.sqlite3"),
}
}


AUTH_PASSWORD_VALIDATORS = [
{"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
{"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
{"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"


REST_FRAMEWORK = {
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.IsAuthenticated",
]
}