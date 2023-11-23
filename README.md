# Proyecto Tamagotchi: Carlito
Repositorio para crear un tamagotchi basado en web y hecho con django. Hecho para Programacion III.

[Analisis previos al desarrollo](./analisis.md)

## Integrantes
- Hilario Yañez
- Tomas Miranda
- Roman Maldonado
- Santino Vitulo

## Dependencias:
- [Django](https://www.djangoproject.com/)
- [django-sass-processor](https://pypi.org/project/django-sass-processor/)

## Configurar DB's del proyecto

Para cambiar el motor de base de datos, actualizar en [settings.py](./carlito/settings.py):

### MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carlito',
        'USER': 'root',
        'PASSWORD': '(..)',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### SQLite

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'carlito.sqlite3',
    }
}
