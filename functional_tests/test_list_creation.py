from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class NewVisitorTest(FunctionalTest):    
    
    def test_can_create_new_list_and_retrieve_new_list(self):
        
    #Jane so really cool app on web and she liked to check it out and she types this url in the address bar
        self.browser.get(self.server_url)


    #Jane sees to-do lists on title and header textx
        self.assertIn('to-do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new to-do list',header_text)
        
#Jane is presented with text box  to add a new task to the list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
#She types "Buy weekly shopping" in the list
        #inputbox.clear()
        inputbox.send_keys('Buy weekly shopping')
        inputbox.send_keys(Keys.RETURN)
        #Jane is taken to her own url for her lists
        jane_list_url = self.browser.current_url
        self.assertRegex(jane_list_url,'/lists/.+')
        #time.sleep(5)
        self.check_for_row_in_list('1: Buy weekly shopping')
        #self.check_for_row_in_list('2: Buy two pints of Milk')
#Jane clicks on the new button and weekly shopping is added to a table list
        #time.sleep(10)
        #self.assertTrue(any(row.text=='1: Buy weekly shopping' for row in rows), 'New item did not appear in list current text is \n%s' % (table.text))
        
        #Second item added by jane 
        inputbox = self.browser.find_element_by_id('id_new_item')
        #self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
#She types "Buy two pints of Milk" in the list
        #inputbox.clear()
        inputbox.send_keys('Buy two pints of Milk')
        inputbox.send_keys(Keys.RETURN)
        #time.sleep(10)
        #Page updates again and Jane sees below 2 items in her own list
        self.check_for_row_in_list('1: Buy weekly shopping')
       # time.sleep(5)
        self.check_for_row_in_list('2: Buy two pints of Milk')
        
        #New user Francis comes along and presented with new url        
        ##We use a new browser session to make sure no session, cokkies etc are being used from previous user
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #New url is presented ot Francis and he can't see any sign of Jane
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy weekly shopping',page_text)
        self.assertNotIn('Buy two pints of Milk',page_text)
        
        #Fracis creates his own new list 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Cheese')
        inputbox.send_keys(Keys.RETURN)
        
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, jane_list_url)
        
        #Again there is no trace od Jane's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy weekly shopping',page_text)
        self.assertNotIn('Buy two pints of Milk',page_text)
        
        #She adds another item to the t-do list
        #self.fail('Finish the test!')
