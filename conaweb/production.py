from .settings import *
ALLOWED_HOSTS=['coopnabomberos.com','www.coopnabomberos.com', '*']
DEBUG=False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'coopnabomberos',
        'USER': 'conabomadmin',
        'PASSWORD': 'CoopNaBomberos2021',
        'HOST': 'localhost',
        'PORT': '',
    }
}