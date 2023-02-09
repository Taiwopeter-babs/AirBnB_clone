#!/usr/bin/python3
"""
    This module contains unit tests for the
    class `BaseModel`
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from io import StringIO
import sys


class TestBaseModel(unittest.TestCase):
    """Test base class for application"""
    
    """
      Set this class attribute for when you need to see
      the difference between your actual output and expected result
    """
    # maxDiff = None

    @classmethod
    def setUpClass(cls):
        """Sets up objects to be used for testing"""
        cls.base_1 = BaseModel()
    
    @classmethod
    def tearDownClass(cls):
        """Tears down or deletes objects after all tests"""
        del cls.base_1

    def test_instance_without_kwargs(self):
        """Test class instance created without kwargs"""
        TestBaseModel.base_1.number = 100
        TestBaseModel.base_1.name = "My Model"

        self.assertIsNotNone(TestBaseModel.base_1.id)
        self.assertIsInstance(TestBaseModel.base_1.id, str)
        self.assertIsNotNone(TestBaseModel.base_1.created_at) 
        self.assertIsNotNone(TestBaseModel.base_1.updated_at)

        # Test created attributes
        self.assertIsNotNone(TestBaseModel.base_1.number)
        self.assertIsNotNone(TestBaseModel.base_1.name)

        self.assertIsInstance(TestBaseModel.base_1.number, int)
        self.assertIsInstance(TestBaseModel.base_1.name, str)
        
        # Test save() method with updated time
        first_updated_time = TestBaseModel.base_1.updated_at
        TestBaseModel.base_1.save()
        second_updated_time = TestBaseModel.base_1.updated_at

        self.assertNotEqual(second_updated_time, first_updated_time)

    def test_dict_method(self):
        """Test to_dict method of class"""
        TestBaseModel.base_1.number = 100
        base_dict = TestBaseModel.base_1.to_dict()

        self.assertIsInstance(base_dict, dict)
        self.assertIn("__class__", base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)
        self.assertIsInstance(base_dict["number"], int)

    def test_instance_from_kwargs(self):
        """Test instance created from kwargs"""
        TestBaseModel.base_1.number = 100
        TestBaseModel.base_1.name = "Test Model"
        base_dict = TestBaseModel.base_1.to_dict()
        base_2 = BaseModel(**base_dict)
        
        self.assertIsInstance(base_2, BaseModel)
        self.assertEqual(base_2.id, TestBaseModel.base_1.id)
        self.assertEqual(base_2.created_at, TestBaseModel.base_1.created_at)
        self.assertEqual(base_2.updated_at, TestBaseModel.base_1.updated_at)

        self.assertEqual(base_2.number, TestBaseModel.base_1.number)
        self.assertEqual(base_2.name, TestBaseModel.base_1.name)
        self.assertNotIn("__class__", base_2.__dict__)
        self.assertIsNot(base_2, TestBaseModel.base_1)

        self.assertIsInstance(base_2.created_at, datetime)
        self.assertIsInstance(base_2.updated_at, datetime)

    def test_str_method(self):
        """
            This tests the __str__ magic method
            by using show_output() function
        """
        model = BaseModel()

        _str_output = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                            model.__dict__)
        output = TestBaseModel.show_output(model)

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

