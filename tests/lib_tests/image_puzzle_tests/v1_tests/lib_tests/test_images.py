""" 
    Test Images file for unit testing
"""
import os
import sys
import re
import random
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(
    os.path.realpath(__file__)) + '/../../../../../lib'))

from image_puzzle.v1.lib.images import Images


class TestInterfaceNamesAbbreviate(unittest.TestCase):
    
    def setUp(self):
        """ unittest setUp """
        self.images = Images()

    def test__create_random_url(self):
        """ test the _create_random_url method """
        result = self.images._create_random_url()
        self.assertTrue(re.search(self.images._base_url % '\d+', result))

    def test_get_image(self):
        """ test the get_image method """
        image_id = 0
        result = self.images.get_image(image_id)
        self.assertTrue(re.search(self.images._base_url % '\d+', result[0]))
        self.assertEquals(result[1], 'Successful URL found.')

    def test_get_image_dne(self):
        """ test the get_image method for dne """
        image_id = len(self.images._image_urls) + 1
        result = self.images.get_image(image_id)
        self.assertEquals(result[0], None)
        self.assertEquals(result[1], "Url index does not exist: '%i'"
            % image_id)

    def test_get_image_random(self):
        """ test the get_image_random method """
        result = self.images.get_image_random()
        self.assertTrue(re.search(self.images._base_url % '\d+', result[0]))
        self.assertEquals(result[1], 'Successful URL found.')

    def test_get_images(self):
        """ test the get_images method """
        start = 5
        limit = 20
        result = self.images.get_images(start, limit)
        self.assertTrue(re.search(self.images._base_url % '\d+', result[0][0]))
        self.assertEquals(limit, len(result[0]))
        self.assertEquals(result[1], "%i Successful URLs found." % limit)


if __name__ == "__main__":
    unittest.main()
