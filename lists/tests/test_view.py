from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page, view_list
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, List

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

       
class ListViewTest(TestCase):
    
    def test_uses_list_template(self):
        list_ = List.objects.create()
        list_response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(list_response, 'list.html')
    
    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()    
        Item.objects.create(text='itemy 1', list=correct_list)
        Item.objects.create(text='itemy 2', list=correct_list)
        other_list = List.objects.create()      
        Item.objects.create(text='Other list itemy 1', list=other_list)
        Item.objects.create(text='Other list itemy 2', list=other_list)
        
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response, 'itemy 1')
        self.assertContains(response,'itemy 2')
        self.assertNotContains(response,'Other list itemy 1')
        self.assertNotContains(response,'Other list itemy 2')

    def test_passes_correct_list_to_templates(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)


class NewListView(TestCase):
    
    def test_to_save_POST_request(self):        
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post('/lists/%d/new_item' % (correct_list.id,), data={'item_text': 'A new list item'})
        
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, correct_list)
        
    def test_redirection_after_post(self):       
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post('/lists/%d/new_item' % (correct_list.id,), data={'item_text': 'A new list item'})
        #self.assertEqual(response.status_code, 302)
        #new_list = List.objects.first()
        self.assertRedirects(response,'/lists/%d/' % (correct_list.id,))
        
        #self.assertIn('A new list item', response.content.decode())
        #expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        #self.assertEqual(response.content.decode(), expected_html)

        
        
        