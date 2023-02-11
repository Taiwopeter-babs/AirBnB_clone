#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `User`
"""
from models.user import User
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestUser(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.user_1 = User()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.user_1

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.user_1.email = "test@gmail.com"
        self.user_1.password = "password"
        self.user_1.first_name = "Taiwo"

        self.assertEqual(self.user_1.email, "test@gmail.com")
        self.assertEqual(self.user_1.password, "password")
        self.assertEqual(self.user_1.first_name, "Taiwo")
        self.assertEqual(len(self.user_1.last_name), 0)

        self.assertIsNotNone(self.user_1.id)
        self.assertIsInstance(self.user_1.id, str)
        self.assertIsNotNone(self.user_1.created_at)
        self.assertIsNotNone(self.user_1.updated_at)

        self.assertIsInstance(self.user_1.created_at, datetime)
        self.assertIsInstance(self.user_1.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.user_1.email = "test@gmail.com"

        user_dict = self.user_1.to_dict()
        new_user = User(**user_dict)

        self.assertIsInstance(new_user.id, str)
        self.assertEqual(new_user.email, "test@gmail.com")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

        self.assertEqual(new_user.password, self.user_1.password)
        self.assertEqual(new_user.first_name, self.user_1.first_name)

        self.assertEqual(new_user.created_at, self.user_1.created_at)
        self.assertEqual(new_user.updated_at, self.user_1.updated_at)
        self.assertEqual(new_user.id, self.user_1.id)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        user_dict = self.user_1.to_dict()
        new_user = User(**user_dict)

        self.assertIsNot(new_user, self.user_1)

        self.assertNotIn("__class__", new_user.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        user_key = "{}.{}".format(type(self.user_1).__name__, self.user_1.id)
        self.assertIn(user_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.user_1.updated_at
        self.user_1.save()
        second_update = self.user_1.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        user_dict = self.user_1.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = User()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestUser.show_output(model)

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
