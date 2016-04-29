"""
.. module::  core_utils_test_models.tests.test_models
   :synopsis: core_utils_test_models models unit test module.

*core_utils_test_models* models unit test module.
"""
from __future__ import absolute_import, print_function

from django.db.models.deletion import ProtectedError
from django.db.utils import IntegrityError

from django_core_utils import constants
from django_core_utils.tests.test_utils import (NamedModelTestCase,
                                                VersionedModelTestCase)

from . import factories
from ..models import MyNamedModel, MyVersionedModel


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

    def verify_derived(self, index, obj):
        # This method overrides base class implementation
        self._verify_derived += 1
        self.assertEqual(index, 0, "invalid index")
        self.assertTrue(obj, "invalid instance")

    def test_version_model_create(self):
        instance = factories.MyVersionedModelFactory()
        self.verify_instance(instance)

    def test_version_version_update(self):
        instance = factories.MyVersionedModelFactory()
        self.verify_instance(instance)
        instance_version = instance.version
        instance.save()
        saved_instance = factories.MyVersionedModel.objects.get(pk=instance.id)
        self.assertEqual(instance_version + 1, saved_instance.version)

    def test_deletion(self):
        instance = factories.MyVersionedModelFactory()
        self.verify_instance(instance)
        self.assertEqual(factories.MyVersionedModel.objects.count(), 1)
        instance.delete()
        with self.assertRaises(MyVersionedModel.DoesNotExist):
            factories.MyVersionedModel.objects.get(pk=instance.id)
        self.assertEqual(factories.MyVersionedModel.objects.count(), 0)

    def test_delete_effective_user(self):
        # Verifies on_protect deletion behavior
        instance = factories.MyVersionedModelFactory()
        self.verify_instance(instance)
        with self.assertRaises(ProtectedError):
            instance.effective_user.delete()
        self.assertTrue(True)


class VersionedModelManagerTestCase(VersionedModelTestCase):
    """Versioned model manager unit test class.
    """

    def test_get_or_none(self):
        instance = factories.MyVersionedModel.objects.get_or_none(pk=1)
        self.assertFalse(instance, "expected none for get_or_none")
        instance = factories.MyVersionedModelFactory()
        self.verify_instance(instance)
        fetched = factories.MyVersionedModel.objects.get_or_none(
            pk=instance.id)
        self.assertEqual(instance, fetched, "unexpected results get_or_none")


class MyNamedModelTestCase(NamedModelTestCase):
    """Sample named model unit test class.
    """
    def test_named_model_create(self):
        expected = 'myname'
        instance = factories.MyNamedModelFactory(name=expected)
        self.verify_instance(instance)
        self.assertEqual(instance.name,
                         expected,
                         "invalid instance name")

    def test_duplicate_name(self):
        name1 = 'myname'
        instance1 = factories.MyNamedModelFactory(name=name1)
        self.verify_instance(instance1)
        instance2 = factories.MyNamedModelFactory(name='abc')
        instance2.name = name1
        with self.assertRaises(IntegrityError):
            instance2.save()


class MyOptionalNamedModelTestCase(NamedModelTestCase):
    """Sample optional named model unit test class.
    """
    def test_named_model_create(self):
        expected = 'myname'
        instance = factories.MyOptionalNamedModelFactory(name=expected)
        self.verify_instance(instance)
        self.assertEqual(instance.name,
                         expected,
                         "invalid instance name")

    def test_duplicate_name(self):
        name1 = 'myname'
        instance1 = factories.MyOptionalNamedModelFactory(name=name1)
        self.verify_instance(instance1)
        instance2 = factories.MyOptionalNamedModelFactory(name='abc')
        instance2.name = name1
        instance2.save()
        self.verify_instance(instance2, version=2)


class NamedModelManagerTestCase(NamedModelTestCase):
    """Named model manager unit test class.
    """

    def test_get_named(self):
        name = 'my name'
        with self.assertRaises(MyNamedModel.DoesNotExist):
            MyNamedModel.objects.named_instance(name=name)

        unknown_instance = factories.MyNamedModelFactory(
            name=constants.UNKNOWN)
        instance = MyNamedModel.objects.named_instance(name=name)
        self.assertEqual(instance,
                         unknown_instance,
                         "expected unknown from  named_instance")
        named_instance = factories.MyNamedModelFactory(name=name)
        fetched = MyNamedModel.objects.named_instance(name=name)
        self.assertEqual(named_instance,
                         fetched,
                         "unexpected results named_instance")


class MyPrioritizedModelTestCase(VersionedModelTestCase):
    """Sample prioritized model unit test class.
    """
    def test_version_model_create(self):
        instance = factories.MyPrioritizedModelFactory()
        self.verify_instance(instance)
        self.assertTrue(instance.priority >= 0,
                        "invalid priority %d" % instance.priority)
