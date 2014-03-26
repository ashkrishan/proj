from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):
    def test_to_find_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_response(self):
        request = HttpRequest()
        response = home_page(request)
        #self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertIn(b'<title>to-do lists</title>', response.content)
        #self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_to_save_POST_request(self):
        request = HttpRequest()        
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)