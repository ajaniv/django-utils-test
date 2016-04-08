"""
.. module::  django_core_utils_test.settings_sqlite
   :synopsis:  Django sqlite settings file.

Django sqlite settings file.

"""
import os
from .settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
