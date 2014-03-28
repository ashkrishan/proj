from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page, view_list
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
#from django.test import client


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
     
    #def test_homepage_only_saves_item_when_necessary(self):
       # request = HttpRequest()
       # home_page(request)
       # self.assertEqual(Item.objects.count(),0)

class ItemModelTest(TestCase):
    def test_to_save_and_retrieve_items(self):
        first_item = Item()
        first_item.text = "The first ever item"
        first_item.save()
        
        second_item = Item()
        second_item.text = "Second item"
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first ever item")
        self.assertEqual(second_saved_item.text, "Second item")
        
class ListViewTest(TestCase):
    
    def test_uses_list_template(self):
        response = self.client.get('/lists/the_only_list_in_the_world/')
        self.assertTemplateUsed(response, 'list.html')
    
    def test_displays_all_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')
        
        #request = HttpRequest()
        #response = view_list(request)
        #self.assertIn('itemy 1', response.content.decode())
        #self.assertIn('itemy 2', response.content.decode())
        
        response = self.client.get('/lists/the_only_list_in_the_world/')
        self.assertContains(response, 'itemy 1')
        self.assertContains(response,'itemy 2')


class NewListView(TestCase):
    
    def test_to_save_POST_request(self):        
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')        
        
    def test_redirection_after_post(self):       
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        #self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/lists/the_only_list_in_the_world/')
        
        #self.assertIn('A new list item', response.content.decode())
        #expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        #self.assertEqual(response.content.decode(), expected_html)
        