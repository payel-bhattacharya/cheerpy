import unittest
from cheerpy.cheerpy import CheerPy

class TestCheerPy(unittest.TestCase):
    
    def setUp(self):
        self.cheerpy = CheerPy()
    
    def test_random_success_message(self):
        message = self.cheerpy.random_success_message()
        self.assertIn(message, self.cheerpy.success_messages)
    
    def test_random_failure_message(self):
        message = self.cheerpy.random_failure_message()
        self.assertIn(message, self.cheerpy.failure_messages)
    
    def test_custom_success_message(self):
        custom_message = "You are amazing! 💫"
        self.cheerpy.add_custom_success_message(custom_message)
        self.assertIn(custom_message, self.cheerpy.success_messages)
    
    def test_custom_failure_message(self):
        custom_message = "Don’t worry, we’ll fix this! 🛠️"
        self.cheerpy.add_custom_failure_message(custom_message)
        self.assertIn(custom_message, self.cheerpy.failure_messages)

if __name__ == '__main__':
    unittest.main()
