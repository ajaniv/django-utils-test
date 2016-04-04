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
* Usage of Sqlite, Postgress, and Mysql to verify proper ORM mappings.

Notes
^^^^^
* pandoc was used to convert from .rst to .md:

  ``pandoc -f rst -t markdown_github -o README.md README.rst``