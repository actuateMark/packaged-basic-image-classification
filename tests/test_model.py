import unittest

from model_lib.model import BasicImageClassifier
from flask_psc_model import ModelBase


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = BasicImageClassifier()

    def test_model_is_model_base_instance(self):
        self.assertIsInstance(self.model, ModelBase)

    # and more comprehensive tests ...


if __name__ == '__main__':
    unittest.main()
