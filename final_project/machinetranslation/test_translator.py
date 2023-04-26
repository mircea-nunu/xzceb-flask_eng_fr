'''
Tests
'''
import unittest

from . import translator

class TestTranslation(unittest.TestCase):
    '''
    Test translation funtions
    '''
    def test_english_to_french_null(self):
        '''
        Test english_to_french()
        '''
        self.assertEqual(translator.english_to_french(''),
        'No text provided') # test when input is null
    def test_english_to_french_hello(self):
        '''
        Test english_to_french()
        '''
        self.assertEqual(translator.english_to_french('Hello'),
        'Bonjour') # test Hello->Bonjour
    def test_french_to_english_null(self):
        '''
        Test french_to_english()
        '''
        self.assertEqual(translator.french_to_english(''),
        'No text provided') # test when input is null
    def test_french_to_english_hello(self):
        '''
        Test french_to_english()
        '''
        self.assertEqual(translator.french_to_english('Bonjour'),
        'Hello') # test Bonjour->Hello

unittest.main()
