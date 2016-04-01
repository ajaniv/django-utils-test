"""
.. module::  utils_test.models
   :synopsis:  utils_test models module

utils_test models module.

"""
from __future__ import absolute_import

from core_utils.models import (NamedModel, PrioritizedModel, VersionedModel,
                               db_table)

from .apps import CoreUtilsTestModelsConfig

_app_label = CoreUtilsTestModelsConfig.name


class MyVersionedModel(VersionedModel):
    """
    Sample versioned model class.
    """
    class Meta(object):
        """Model meta class."""
        app_label = _app_label
        db_table = db_table(_app_label, "MyVersionedModel")


class MyNamedModel(NamedModel):
    """
    Sample named  model class.
    """
    class Meta(object):
        """Model meta class."""
        app_label = _app_label
        db_table = db_table(_app_label, "MyNamedModel")


class MyPrioritizedModel(VersionedModel, PrioritizedModel):
    """
    Sample prioritized model class.
    """
    class Meta(object):
        """Model meta class."""
        app_label = _app_label
        db_table = db_table(_app_label, "MyPrioritizedModel")
