#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `Review`
"""
from models.review import Review
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestReview(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.review = Review()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.review

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertIsInstance(self.review.place_id, str)

        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str)

        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str)

        self.assertFalse(hasattr(self.review, "city_id"))

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.text, "")

        self.review.text = "Taiwo's Airbnb fulfilled me"

        self.assertEqual(self.review.text, "Taiwo's Airbnb fulfilled me")

        self.assertIsNotNone(self.review.id)
        self.assertIsInstance(self.review.id, str)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)

        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.review.text = "Taiwo's Airbnb"

        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)

        self.assertIsInstance(new_review.id, str)
        self.assertEqual(new_review.text, "Taiwo's Airbnb")

        self.assertEqual(new_review.created_at, self.review.created_at)
        self.assertEqual(new_review.updated_at, self.review.updated_at)
        self.assertEqual(new_review.id, self.review.id)

        self.assertIsNot(new_review, self.review)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)

        self.assertNotIn("__class__", new_review.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        review_key = "{}.{}".format(type(self.review).__name__, self.review.id)
        self.assertIn(review_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.review.updated_at
        self.review.save()
        second_update = self.review.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        review_dict = self.review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertIn("__class__", review_dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = Review()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestReview.show_output(model)

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
