from .base import FunctionalTest

   
class ItemValidation(FunctionalTest):
    
    def test_user_cannot_enter_empty_list(self):
        
        self.browser.get(self.server_url)
        #Jane inputs empty name in the text box and hits enter
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        #Page refreshes and shows an error message that input box can't be empty
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You can't have an empty list item")
        #She tries again with soem text and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy Monitor')
        self.check_for_row_in_list('1: Buy Monitor')
    
        #She tries again to enter empty list again and same error shows up
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        #Page checks previous saved list item 
        self.check_for_row_in_list('1: Buy Monitor')
        
        #Error shows up again on empty item
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #Jane corrects itby putting some item
        self.browser.find_element_by_id('id_new_item').send_keys('Buy PC')
        self.check_for_row_in_list('1: Buy Monitor')
        self.check_for_row_in_list('2: Buy PC')
        
        
        self.fail('write me!')
        
    