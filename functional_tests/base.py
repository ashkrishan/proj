from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver
import unittest
import os
import sys


##This is required for live testing server to point to correct port otherwise OS error is thrown by win 7
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8082'
class FunctionalTest(StaticLiveServerCase):
    
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
        #self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)
        
    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def tearDown(self):
        self.browser.quit()
     
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    ##helper function after refactor
    def check_for_row_in_list(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    