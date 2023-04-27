'''
Tests
'''

import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import unittest

import translator

class TestTranslation(unittest.TestCase):
    '''
    Test translation funtions
    '''
    def test_english_to_french_null(self):
        '''
        Test english_to_french()
        '''
        self.assertNotEqual(translator.english_to_french(''),
        '')# test when input is null
        print("englishToFrench - assertNotEqual Test passed")
    def test_english_to_french_hello(self):
        '''
        Test english_to_french()
        '''
        self.longMessage = True
        self.assertEqual(translator.english_to_french('Hello'),
        'Bonjour', 'test_english_to_french_hello') # test Hello->Bonjour
        print("englishToFrench - assertEqual Test passed")
    def test_french_to_english_null(self):
        '''
        Test french_to_english()
        '''
        self.assertNotEqual(translator.french_to_english(''),
        '') # test when input is null
        print("frenchToEnglish - assertNotEqual Test passed")
    def test_french_to_english_hello(self):
        '''
        Test french_to_english()
        '''
        self.assertEqual(translator.french_to_english('Bonjour'),
        'Hello') # test Bonjour->Hello
        print("frenchToEnglish - assertEqual Test passed")
if __name__ == '__main__':
    unittest.main()
