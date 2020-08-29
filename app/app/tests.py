from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        '''test that two no are added together'''

        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(3, 5), 2)
