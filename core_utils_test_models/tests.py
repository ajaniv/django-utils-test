"""
.. module::  utils.tests
   :synopsis: django-utils-test models unit test module.

*django-utils* models unit test module.
"""
from __future__ import print_function

import factory

from core_utils.tests.factories import NamedModelFactory, VersionedModelFactory
from core_utils.tests.test_util import (NamedModelTestCase,
                                        VersionedModelTestCase)

from .models import MyNamedModel, MyPrioritizedModel, MyVersionedModel


class MyVersionedModelFactory(VersionedModelFactory):
    """Sample versioned model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyVersionedModel


class MyVersionedModelTestCase(VersionedModelTestCase):
    """Sample versioned model unit test class.
    """
    def setUp(self):
        super(MyVersionedModelTestCase, self).setUp()
        self._verify_derived = 0
        self._verify_name = 0

    def tearDown(self):
        super(MyVersionedModelTestCase, self).tearDown()
        self.assertEqual(self._verify_derived, 1,
                         "verify_derived not called")

    def test_version_model_create(self):
        instance = MyVersionedModelFactory()
        self.verify_instance(instance)

    def verify_derived(self, index, obj):
        self._verify_derived += 1
        self.assertEqual(index, 0, "invalid index")
        self.assertTrue(obj, "invalid instance")


class MyNamedModelFactory(NamedModelFactory):
    """Sample named model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyNamedModel


class MyNamedModelTestCase(NamedModelTestCase):
    """Sample named model unit test class.
    """
    def test_named_model_create(self):
        expected = 'myname'
        instance = MyNamedModelFactory(name=expected)
        self.verify_instance(instance)
        self.assertEqual(instance.name,
                         expected,
                         "invalid instance name")


class MyPrioritizedModelFactory(VersionedModelFactory):
    """Sample prioritized model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyPrioritizedModel

    priority = factory.Sequence(lambda n: n)


class MyPrioritizedModelTestCase(VersionedModelTestCase):
    """Sample prioritized model unit test class.
    """
    def test_version_model_create(self):
        instance = MyPrioritizedModelFactory()
        self.verify_instance(instance)
        self.assertTrue(instance.priority >= 0,
                        "invalid priority %d" % instance.priority)
