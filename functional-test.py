from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
#import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_crewat_new_list_and_retrieve_new_list(self):
        
    #Jane so really cool app on web and she liked to check it out and she types this url in the address bar
        self.browser.get('http://localhost:8000')


    #Jane sees to-do lists on title and header text
        self.assertIn('to-do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('to-do lists',header_text)
        
#Jane is presented with text box and button to add a new task to the list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
#She types "Buy weekly shopping" in the list
        inputbox.clear()
        inputbox.send_keys('Buy weekly shopping')
        inputbox.send_keys(Keys.RETURN)

#Jane clicks on the new button and weekly shopping is added to a table list
        #time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: Buy weekly shopping' for row in rows))
        
        #She adds another item to the t-do list
        self.fail('Finish the test!')
        
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    