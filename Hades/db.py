import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

{
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    "default" : {
        "ENGINE" : "django.db.backends.postgresql_psycopg2",
        "NAME" : "db",
        "USER" : "postgres",
        "PASSWORD" : "qwe123",
        "HOST" : "localhost",
        "PORT" : "5432"
    }
}