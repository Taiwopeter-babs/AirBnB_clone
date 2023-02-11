#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `State`
"""
from models.state import State
from models import storage
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestState(unittest.TestCase):
    """Test base class for application"""

    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    def setUp(self):
        """Sets up objects to be used for testing"""
        self.state = State()

    def tearDown(self):
        """Tears down or deletes objects after all tests"""
        del self.state

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        self.assertEqual(self.state.name, "")

        self.state.name = "Lagos"

        self.assertEqual(self.state.name, "Lagos")

        self.assertIsNotNone(self.state.id)
        self.assertIsInstance(self.state.id, str)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_instance_created_from_dict(self):
        """Test instance created from kwargs"""
        self.state.name = "Osun"

        state_dict = self.state.to_dict()
        new_state = State(**state_dict)

        self.assertIsInstance(new_state.id, str)
        self.assertEqual(new_state.name, "Osun")

        self.assertEqual(new_state.created_at, self.state.created_at)
        self.assertEqual(new_state.updated_at, self.state.updated_at)
        self.assertEqual(new_state.id, self.state.id)

        self.assertIsNot(new_state, self.state)

    def test_class_not_in_instance_from_dict(self):
        """test __class__ attribute not in object created from kwargs"""
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)

        self.assertNotIn("__class__", new_state.__dict__)

    def test_new_method(self):
        """Test the `new` method called in constructor of parent class"""
        state_key = "{}.{}".format(type(self.state).__name__, self.state.id)
        self.assertIn(state_key, storage.all())

    def test_save_method(self):
        """Test that time is updated"""
        first_update = self.state.updated_at
        self.state.save()
        second_update = self.state.updated_at

        self.assertNotEqual(first_update, second_update)

    def test_dict_method(self):
        """Test to_dict method"""
        state_dict = self.state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_str_method(self):
        """test printed output"""
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = State()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                              model.__dict__)
        output = TestState.show_output(model)

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
