# -*- coding: utf-8 -*-
import unittest
import cifar10_deep.models.deepaas_api as deepaas_api

class TestModelMethods(unittest.TestCase):
    
    def setUp(self):
        self.meta = deepaas_api.get_metadata()
        
    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)
        
    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['Name'].replace('-','').replace('_',''),
                        'cifar10_deep'.replace('-','').replace('_',''))
        self.assertEqual(self.meta['Author'], 'L.Lloret, V.Kozlov')
        self.assertEqual(self.meta['Author-email'], 'valentin.kozlov@kit.edu')


if __name__ == '__main__':
    unittest.main()
