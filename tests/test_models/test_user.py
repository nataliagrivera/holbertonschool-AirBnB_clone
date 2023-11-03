#!/usr/bin/python3

import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test for the User class in the 'models.user' module.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to create a User instance with initial attributes.
        """
        cls.my_user = User()
        cls.my_user.first_name = "John"
        cls.my_user.last_name = "Doe"
        cls.my_user.email = "123@holbertonshool.com"
        cls.my_user.password = "password"

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to clean up after testing.
        This method is called after all test methods have been executed.
        It removes the User instance and deletes the 'file.json' if it exists.
        """
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test if User is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Test if the User class has a docstring.
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """
        Test if User class instance has the expected attributes.
        """
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if User class instance attributes are of type str.
        """
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        """
        Test the 'save' method of the User class.
        It checks if 'created_at' and 'updated_at' are not equal after saving.
        """
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """
        Test if the 'to_dict' method is available for the User class.
        """
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
