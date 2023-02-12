#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `City`
"""
from models.city import City
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestCity(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.city = City()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.city

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.assertEqual(self.city.name, "")

        self.city.name = "Lagos"

        self.assertEqual(self.city.name, "Lagos")

        self.assertIsNotNone(self.city.id)
        self.assertIsInstance(self.city.id, str)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)

        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.city.name = "Osun"

        city_dict = self.city.to_dict()
        new_city = City(**city_dict)

        self.assertIsInstance(new_city.id, str)
        self.assertEqual(new_city.name, "Osun")

        self.assertEqual(new_city.created_at, self.city.created_at)
        self.assertEqual(new_city.updated_at, self.city.updated_at)
        self.assertEqual(new_city.id, self.city.id)

        self.assertIsNot(new_city, self.city)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)

        self.assertNotIn("__class__", new_city.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        city_key = "{}.{}".format(type(self.city).__name__, self.city.id)
        self.assertIn(city_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.city.updated_at
        self.city.save()
        second_update = self.city.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        city_dict = self.city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = City()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestCity.show_output(model)

        self.assertEqual(output.getvalue(), _str_output)

    @staticmethod
    def show_output(instance_of_class):
        """
            Test the __str__ magic method in class
            This returns the captured output of stdout
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        print(instance_of_class)

        sys.stdout = sys.__stdout__

        return (captured_output)
