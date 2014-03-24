from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    def test_to_find_failure(self):
        self.assertEqual(1 + 1, 3)
        