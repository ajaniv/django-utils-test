"""
.. module::  django_core_utils_test.settings_test
   :synopsis:  Django test settings file.

Django test settings file.

"""
from __future__ import print_function
from os import getenv
from .settings import *  # @UnusedWildImport


DB_ENGINE_SQLITE = 'sqlite'
DB_ENGINE_POSTGRES = 'postgres'
DB_ENGINE_MYSQL = 'mysql'
db_engine = getenv('DB_ENGINE', DB_ENGINE_SQLITE)
print('Using db_engine', db_engine)
if db_engine == DB_ENGINE_POSTGRES:
    from .settings_postgres import *  # @UnusedWildImport
elif db_engine == DB_ENGINE_MYSQL:
    from .settings_mysql import *  # @UnusedWildImport
else:
    from .settings_sqlite import *  # @UnusedWildImport
