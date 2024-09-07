# tests/__init__.py

import unittest
from tests.test_haplotyper import TestHaplotyper

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHaplotyper))
    return suite