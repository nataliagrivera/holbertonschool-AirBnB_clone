#!/usr/bin/python3

import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    This class contains unit tests for the State class and its functionalities.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class by creating an instance of the State class and initializing some attributes.
        """
        cls.state1 = State()
        cls.state1.name = "Alaska"

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after the test class by deleting the State instance and removing the JSON data file if it exists.
        """
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Check if the State class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Check if the State class has a docstring.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """
        Check if the State instance has the expected attributes.
        """
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """
        Verify that the 'name'attribute of the State instance is a string.
        """
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        """
        Test the 'save' method to ensure that 'create_at' and 'updated_at' attributes are not equal after saving.
        """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """
        Check if the 'to_dict' method is defined for the State instance.
        """
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
