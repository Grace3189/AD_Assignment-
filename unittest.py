import self
from PIL import Image
from unittest import TestCase
from clothingsuggestion import ClothingSuggestionApp


class ClothingSuggestionApp1:
    def __init__(self):
        self.app = None

    def setUp(self):
        self.app = ClothingSuggestionApp()

    def test_get_user_input(self):
        self.app.get_user_input()
        self.assertEqual(self.app.gender, "Male")
        self.assertEqual(self.app.age, 25)
        self.assertEqual(self.app.country, 3)
        self.assertEqual(self.app.weather, 2)

        def assertEqual(self, gender, param):
            pass


