'''
Tests
'''
import unittest

from . import translator

class TestTranslation(unittest.TestCase):
    '''
    Test translation funtions
    '''
    def test1(self):
        '''
        Test englishToFrench()
        '''
        self.assertEqual(translator.englishToFrench(''), 'No text provided') # test when input is null
        self.assertEqual(translator.frenchToEnglish(''), 'No text provided') # test when input is null

unittest.main()
