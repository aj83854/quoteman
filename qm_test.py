import unittest
from quoteman import make_soup_from, get_quotes
import requests
from bs4 import BeautifulSoup

target_url = "http://quotes.toscrape.com"

class ScraperTests(unittest.TestCase):

    def test_source_host_is_available(self):
        """Check to see that the target_url is online/available."""
        response = requests.get(target_url)
        self.assertEqual(response.status_code, 200)

    def test_soup(self):
        """
        Ensure object made from 'make_soup_from_source' 
        is of BeautifulSoup type.
        """
        soup_obj = make_soup_from(target_url)
        self.assertIsInstance(soup_obj, BeautifulSoup)

if __name__ == "__main__":
    unittest.main()
