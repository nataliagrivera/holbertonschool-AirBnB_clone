#!/usr/bin/python3

import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment for the Place class.
        """
        cls.place1 = Place()
        cls.place1.city_id = "Somewhere in Alaska"
        cls.place1.user_id = "John"
        cls.place1.name = "Columbia Glacier"
        cls.place1.description = "Alaska's most famous glacier"
        cls.place1.number_rooms = 0
        cls.place1.number_bathrooms = 0
        cls.place1.max_guest = 0
        cls.place1.price_by_night = 0
        cls.place1.latitude = 0.0
        cls.place1.longitude = 0.0
        cls.place1.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test enviroment for the Place class
        """
        del cls.place1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test if Place is a subclass of a BaseModel.
        """
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Test if Place has a docstring.
        """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """
        Test if Place class has the required attributes.
        """
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if the attributes of Place class have the correct data types.
        """
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_save(self):
        """
        Test if the save method updates the 'update_at' attribute.
        """
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        """
        Test if the 'to_dict' method is present in the Place class.
        """
        self.assertEqual('to_dict' in dir(self.place1), True)


if __name__ == "__main__":
    unittest.main()
