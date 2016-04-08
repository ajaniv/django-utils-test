======================
django-core-utils-test
======================

*django-core-utils-test* is a Django project to test *django-core-utils*  
abstract model classes.  It uses a bare bones Django settings and application
to achieve the following:

* Testing of model classes derived from abstract base classes.  It is somewhat tricky
  to create model classes as part of a Django unit test.  It requires 'forcing' Django
  to generate the database tables through custom migration, manual low level SQL generation
  constructs, or a similar approach, which would like be incompatible with a future
  Django release.
* Usage of *Sqlite*, *Postgres*, and *Mysql* using docker to verify proper ORM mappings
  in a python 3.5 environment.
* Usage of tox to verify proper behavior using sqlite under several Python and Django versions.

Notes
^^^^^
* pandoc was used to convert from .rst to .md:

  ``pandoc -f rst -t markdown_github -o README.md README.rst``
* Use `eval config_env.sh` to set environment variables for running commands such as `python manage.py test`.
* To run unit tests in docker sqlite environment: `docker-compose -f docker-compose-sqlite.yml up --abort-on-container-exit` .
* To run unit tests in docker postgres environment: `docker-compose -f docker-compose-postgres.yml up --abort-on-container-exit` .
* To run unit tests in docker mysql environment: `docker-compose -f docker-compose-mysql.yml up --abort-on-container-exit` .
  