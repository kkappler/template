"""
    Test for grid stuffs.
    
    TODO: add a test that shows how a TensorMesh can be used to match an NDGrid
"""

import unittest

from template.util.helper_functions import execute_subprocess


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.some_reused_value = 0.0

    def setUp(self):
        pass

    def test_execute_subprocess(self):
        cmd = "ls"
        result = execute_subprocess(cmd)
        print(result)
        assert (result is not None)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

# =============================================================================
#
# =============================================================================
if __name__ == "__main__":
    unittest.main()

