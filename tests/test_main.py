"""Unit tests for main module.

This module contains the unit tests for the main module.
"""

import unittest
import main

class TestMain(unittest.TestCase):
    """Tests for main module."""

    def test_main(self):
        """Test main function."""
        config_path = 'path/to/test/config'
        output_dir = 'path/to/test/output'
        success = main.main(config_path, output_dir)
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()