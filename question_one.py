import unittest

class BaseClass:
    def __init__(self, prop1, prop2, prop3):
        """
        Initialize the base class with three properties.
        :param prop1: First property, can be any data type.
        :param prop2: Second property, can be any data type.
        :param prop3: Third property, can be any data type.
        """
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3

    @classmethod
    def empty_class_method(cls):
        """
        An empty class method.
        This can be used for class-level operations in the future.
        """
        pass

    def empty_instance_method(self):
        """
        An empty instance method.
        This can be utilized for instance-specific operations in the future.
        """
        pass


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.test_object = BaseClass('value1', 'value2', 'value3')

    def test_initialization(self):
        """
        Test if the properties are correctly initialized.
        """
        self.assertEqual(self.test_object.prop1, 'value1')
        self.assertEqual(self.test_object.prop2, 'value2')
        self.assertEqual(self.test_object.prop3, 'value3')

    def test_empty_class_method(self):
        """
        Test the empty class method.
        Since it's empty, we're just ensuring it exists and is callable.
        """
        self.assertIsNone(BaseClass.empty_class_method())

    def test_empty_instance_method(self):
        """
        Test the empty instance method.
        Similar to the class method, we're testing its existence and callability.
        """
        self.assertIsNone(self.test_object.empty_instance_method())
