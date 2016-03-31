"""
.. module::  utils.tests
   :synopsis: django-utils-test models unit test module.

*django-utils* models unit test module.
"""
from __future__ import print_function

from .models import MyVersionedModel
from core_utils.tests.factories import VersionedModelFactory
from core_utils.tests.test_util import VersionedModelTestCase


class MyVersionedModelFactory(VersionedModelFactory):
    class Meta(object):
        model = MyVersionedModel


class MyVersionedModelTestCase(VersionedModelTestCase):

    def test_version_model_create(self):
        instance = MyVersionedModelFactory()
        self.assertEqual(instance.version, 1)
        self.assertTrue(MyVersionedModel.objects.get(pk=instance.id))
