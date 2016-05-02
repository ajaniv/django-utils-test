"""
.. module::  core_utils_test_models.tests.test_serializers
   :synopsis: core_utils_test_models serializers unit test module.

*core_utils_test_models* serializers unit test module.
"""
from __future__ import absolute_import, print_function

import collections

from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from django_core_utils.serializers import NamedModelSerializer

from ..models import MyNamedModel
from .factories import MyNamedModelFactory


class MyNamedModelSerializer(NamedModelSerializer):
    """Sample serializer class."""
    class Meta(NamedModelSerializer.Meta):
        """Meta class definition."""
        model = MyNamedModel


class NamedModelSerializerTestCase(TestCase):
    """Named model serializer unit test class.

    This unit test is designed to verify basic integration
    with Django's rest framework components.
    """
    def test_model_serialization(self):

        instance_1 = MyNamedModelFactory(name="my_name")
        instance_1.save()
        serializer_1 = MyNamedModelSerializer(instance_1)
        serialized_data = serializer_1.data
        self.assertTrue(isinstance(serialized_data, dict),
                        "serialized data is not dict")
        content = JSONRenderer().render(serialized_data)
        self.assertTrue(isinstance(content, bytes),
                        'content is not bytes')
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        self.assertTrue(isinstance(data, dict),
                        "de-serialized data is not dict")
        # changing name field is required due to its unique constraints
        # which is causing validation error
        data["name"] = "changed_named"
        serializer_2 = MyNamedModelSerializer(data=data)

        self.assertTrue(serializer_2.is_valid())
        self.assertTrue(serializer_2.validated_data)
        self.assertTrue(isinstance(serializer_2.validated_data,
                                   collections.OrderedDict),
                        "validated data is not ordered dict")
        instance_2 = serializer_2.save()
        self.assertTrue(instance_2, "Failed to save de-serialized instance")
