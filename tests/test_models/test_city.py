#!/usr/bin/python3

import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test case class for the City model.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to create a City instance and set initial attributes.
        """
        cls.city1 = City()
        cls.city1.name = "Anchorage"
        cls.city1.state_id = "AK"

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to remove test instance and cleanup resources.
        """
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test if City is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Test if City class has a docstring.
        """
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """
        Test if City instance has the required attributes.
        """
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if the 'name' and 'state_id' attributes are of type str.
        """
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        """
        Test if the 'save' method updates the 'updated_at' attribute.
        """
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """
        Test if 'to_dict' method is present in the City instance.
        """
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
