from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_crewat_new_list_and_retrieve_new_list(self):
        
    #Jane so really cool app on web and she liked to check it out and she types this url in the address bar
        self.browser.get('http://localhost:8000')


    #Jane sees to-do lists on title
        self.assertIn('to-do lists', self.browser.title)
        self.fail('Finish the tests!')
#Jane is presented with text box and button to add a new task to the list

#She types weekly shopping in the list

#Jane clicks on the new button and weekly shopping is added to the list


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    