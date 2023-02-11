#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `Place`
"""
from models.place import Place
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestPlace(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.place = Place()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.place

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertIsInstance(self.place.city_id, str)

        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertIsInstance(self.place.user_id, str)

        self.assertTrue(hasattr(self.place, "name"))
        self.assertIsInstance(self.place.name, str)

        self.assertTrue(hasattr(self.place, "description"))
        self.assertIsInstance(self.place.description, str)

        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertIsInstance(self.place.number_rooms, int)

        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertIsInstance(self.place.number_bathrooms, int)

        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertIsInstance(self.place.max_guest, int)

        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertIsInstance(self.place.price_by_night, int)

        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertIsInstance(self.place.latitude, float)

        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertIsInstance(self.place.longitude, float)

        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.assertEqual(self.place.name, "")

        self.place.name = "Taiwo's Airbnb"

        self.assertEqual(self.place.name, "Taiwo's Airbnb")

        self.assertIsNotNone(self.place.id)
        self.assertIsInstance(self.place.id, str)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)

        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.place.name = "Taiwo's Airbnb"

        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)

        self.assertIsInstance(new_place.id, str)
        self.assertEqual(new_place.name, "Taiwo's Airbnb")

        self.assertEqual(new_place.created_at, self.place.created_at)
        self.assertEqual(new_place.updated_at, self.place.updated_at)
        self.assertEqual(new_place.id, self.place.id)

        self.assertIsNot(new_place, self.place)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)

        self.assertNotIn("__class__", new_place.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        place_key = "{}.{}".format(type(self.place).__name__, self.place.id)
        self.assertIn(place_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.place.updated_at
        self.place.save()
        second_update = self.place.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        place_dict = self.place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertIn("__class__", place_dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = Place()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestPlace.show_output(model)

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
