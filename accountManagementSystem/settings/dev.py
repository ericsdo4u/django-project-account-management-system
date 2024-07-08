from .general import *

SECRET_KEY = 'django-insecure-0n))88o$xmjd4(%*=mtv&_on+vn+m=4$t1lspqe81g@x#h1$s6'

DEBUG = True


ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'account_db',
        'USER': 'root',
        'PASSWORD': 'Business@1',
        'HOST': 'localhost'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'info@jagudabank.com'
