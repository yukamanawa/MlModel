# test_mlmodelforge.py
"""
Tests for MlModelForge module.
"""

import unittest
from mlmodelforge import MlModelForge

class TestMlModelForge(unittest.TestCase):
    """Test cases for MlModelForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MlModelForge()
        self.assertIsInstance(instance, MlModelForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MlModelForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
