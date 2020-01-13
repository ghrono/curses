#!/usr/bin/env python3.8

import unittest

def mul(x,y):
    return x*y

class My_test(unittest.TestCase):
    def test_uno(self):
        return self.assertEqual(mul(2,5), 8)
    
unittest.main()


