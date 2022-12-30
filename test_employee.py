from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Dan","Nad",2000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,7000)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(3000)
        self.assertEqual(self.employee.salary,5000)

if __name__=="__main__":
    unittest.main()