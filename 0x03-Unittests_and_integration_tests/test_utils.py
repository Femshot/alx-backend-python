#!/usr/bin/env python3
''' Module containing a TestAccessNestedMap class '''
import unittest
from utils import access_nested_map as anm
from parameterized import parameterized
#from typing import (Mapping, Sequence, Any, Dict, Callable,)


"""
class TestAccessToNestedMap(unittest.TestCase):
    ''' Unitest test for Nested map access function '''
    # @parameterized.expand()
    def test_access_nested_map(self, ):
        ''' Test for access_nested_map function return values'''
        self.assertEqual(anm({'a': 1}, ('a',)), 1)
        self.assertEqual(anm({'a': {'b': 2}}, ('a',)), {'b': 2})
        self.assertEqual(anm({'a': {'b': 2}}, ('a', 'b')), 2)
"""
class TestAccessNestedMap(unittest.TestCase):
    ''' Unitest test for Nested map access function '''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' Test for access_nested_map function return values'''
        self.assertEqual(anm(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' Test for Keyerror raise with input value '''
        with self.assertRaises(KeyError):
            anm(nested_map, path)
