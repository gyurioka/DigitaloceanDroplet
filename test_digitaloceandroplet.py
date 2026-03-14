# test_digitaloceandroplet.py
"""
Tests for DigitaloceanDroplet module.
"""

import unittest
from digitaloceandroplet import DigitaloceanDroplet

class TestDigitaloceanDroplet(unittest.TestCase):
    """Test cases for DigitaloceanDroplet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitaloceanDroplet()
        self.assertIsInstance(instance, DigitaloceanDroplet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitaloceanDroplet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
