"""
.. module::  core_utils_test_models.tests.factories
   :synopsis: core_utils_test_models factories module.

*core_utils_test_models* factories module.
"""
from __future__ import absolute_import, print_function

import factory

from django_core_utils.tests.factories import (NamedModelFactory,
                                               VersionedModelFactory)

from ..models import (MyNamedModel, MyOptionalNamedModel, MyPrioritizedModel,
                      MyVersionedModel)


class MyVersionedModelFactory(VersionedModelFactory):
    """Sample versioned model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyVersionedModel


class MyNamedModelFactory(NamedModelFactory):
    """Sample named model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyNamedModel


class MyOptionalNamedModelFactory(NamedModelFactory):
    """Sample optional named model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyOptionalNamedModel


class MyPrioritizedModelFactory(VersionedModelFactory):
    """Sample prioritized model factory class.
    """
    class Meta(object):
        """Model meta class."""
        model = MyPrioritizedModel

    priority = factory.Sequence(lambda n: n)
