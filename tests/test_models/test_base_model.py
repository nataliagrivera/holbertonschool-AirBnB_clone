#!/usr/bin/python3

import unittest
from datetime import datetime
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.bm = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.bm, BaseModel)
        self.assertIsNotNone(self.bm.id)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.bm.id, self.bm.__dict__)
        self.assertEqual(str(self.bm), expected_str)

    def test_save(self):
        original_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(original_updated_at, self.bm.updated_at)

    def test_to_dict(self):
        obj_dict = self.bm.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_kwarg_init(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-02T00:00:00.000000',
            'name': 'TestObject'
        }
        bm = BaseModel(**data)
        self.assertEqual(bm.id, '123')
        self.assertEqual(bm.created_at, datetime(2022, 1, 1))
        self.assertEqual(bm.updated_at, datetime(2022, 1, 2))
        self.assertEqual(bm.name, 'TestObject')

if __name__ == "__main__":
    unittest.main()
