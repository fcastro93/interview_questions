import logging
from question_one import BaseClass

# Basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DerivedClass(BaseClass):
    def __init__(self, prop1, prop2, prop3):
        """
        Initialize the derived class with modified properties.
        :param prop1: First property, can be any data type. Modified in some way.
        :param prop2: Second property, can be any data type. Modified in some way.
        :param prop3: Third property, can be any data type. Modified in some way.
        """
        modified_prop1 = prop1 + "_modified"
        modified_prop2 = prop2 + "_modified"
        modified_prop3 = prop3 + "_modified"

        super().__init__(modified_prop1, modified_prop2, modified_prop3)
        logging.info("DerivedClass initialized with modified properties")

    @classmethod
    def empty_class_method(cls):
        """
        An implemented class method in the derived class.
        """
        logging.info("Class method action performed in DerivedClass")
        return "Class method action performed"

    def empty_instance_method(self):
        """
        An implemented instance method in the derived class.
        """
        logging.info("Instance method action performed in DerivedClass")
        return "Instance method action performed"


# Demonstration of the DerivedClass with logging
if __name__ == '__main__':
    derived_instance = DerivedClass("prop1", "prop2", "prop3")
    DerivedClass.empty_class_method()
    derived_instance.empty_instance_method()
