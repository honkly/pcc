import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        self.my_employee = Employee('knight', 'lee', 10000)
        
    def test_give_default_raise(self):
        """Test a default raise."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.money, 15000)
        
        
    def test_give_custom_raise(self):
        """Test that three individual responses are stored properly."""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.money, 20000)

            
unittest.main()
