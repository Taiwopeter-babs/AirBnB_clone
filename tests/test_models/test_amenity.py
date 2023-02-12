#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `Amenity`
"""
from models.amenity import Amenity
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestAmenity(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.amenity

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.assertEqual(self.amenity.name, "")

        self.amenity.name = "Two bedrooms"

        self.assertEqual(self.amenity.name, "Two bedrooms")

        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.amenity.name = "Two bedrooms"

        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)

        self.assertIsInstance(new_amenity.id, str)
        self.assertEqual(new_amenity.name, "Two bedrooms")

        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)
        self.assertEqual(new_amenity.id, self.amenity.id)

        self.assertIsNot(new_amenity, self.amenity)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)

        self.assertNotIn("__class__", new_amenity.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        amenity_key = "{}.{}".format(type(self.amenity).__name__,
                                     self.amenity.id)
        self.assertIn(amenity_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.amenity.updated_at
        self.amenity.save()
        second_update = self.amenity.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = Amenity()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestAmenity.show_output(model)

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
