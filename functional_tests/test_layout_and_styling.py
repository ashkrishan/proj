from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):    
    
    def test_layout_and_styling(self):
        #Jane goes to the homepage
        self.browser.get(self.server_url)        
        self.browser.set_window_size(1024, 768)
        #she notices page is well aligned
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 505,delta=5)
        #She add the list and sees the list is centred        
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        #self.browser.set_window_size(1024, 768)
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 505, delta=5)
        
    