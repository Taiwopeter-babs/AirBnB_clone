#!/usr/bin/python3
"""
    This module tests the class `FileStorage` methods
"""
import unittest
import os
import json
import pathlib
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """Test storage engine"""

    maxDiff = None
    
    def setUp(self):
        """Sets up instances for test"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        self.store = FileStorage()

    def tearDown(self):
        """Deletes instances created for tests"""
        del self.base1
        del self.base2
        del self.store
    
    def test_private_attributes(self):
        """Test that private attributes can't be accessed"""

        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)

    def test_can_save_instances(self):
        """
            Test that created instances are saved in FileStorage.__objects.
            This test encompasses new, all, and save methods.
            The new method is called in the constructor in each of 
            the instance class.
        """
        self.store.new(self.base1)
        self.store.new(self.base2)


        base1_key = "{}.{}".format(type(self.base1).__name__, self.base1.id)
        base2_key = "{}.{}".format(type(self.base2).__name__, self.base2.id)

        saved_objs = self.store.all()
        
        self.assertIsInstance(saved_objs, dict)
        self.assertIn(base1_key, saved_objs)
        self.assertIn(base2_key, saved_objs)

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        # save the new objects
        self.store.save()

        with open("file.json", "r", encoding="utf-8") as myfile:
            content = myfile.read()
        objs_dict = json.loads(content)

        self.assertIn(base1_key, objs_dict)
        self.assertIn(base2_key, objs_dict)

    def test_reload_objs(self):
        """
            Tests the reload method; the method deserializes the
            objects from the JSON file and stores them in FileStorage.__objects
            with the `new` method
        """
        self.store.new(self.base1)
        self.store.new(self.base1)

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        # save the new objects
        self.store.save()
        # Use created method for file check
        file_path = pathlib.Path("file.json")
        self.assertFileExists(file_path) is True
        
        # Reload objs from JSON file
        self.store.reload()

        saved_objs = self.store.all()

        for obj_key in saved_objs.keys():
            self.assertNotIn("__class__", saved_objs[obj_key].__dict__)

    # create method to assert file existence
    def assertFileExists(self, path):
        """Extends unittest.TestCase with additional assertion"""
        if not pathlib.Path(path).resolve().is_file():
            return False
        return True
