from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_to_find_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        