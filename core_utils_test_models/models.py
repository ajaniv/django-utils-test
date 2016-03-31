"""
.. module::  utils_test.models
   :synopsis:  utils_test models module

utils_test models module.

"""
from __future__ import absolute_import
from core_utils.models import db_table
from core_utils.models import VersionedModel, NamedModel
from core_utils import fields


from .apps import CoreUtilsTestModelsConfig

_app_label = CoreUtilsTestModelsConfig.name


class MyVersionedModel(VersionedModel):
    class Meta(object):
        app_label = _app_label
        db_table = db_table(_app_label, "MyVersionedModel")
