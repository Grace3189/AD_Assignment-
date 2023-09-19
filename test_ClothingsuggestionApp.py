from unittest import TestCase

from Test import ClothingSuggestionApp


class TestClothingSuggestionApp(TestCase):
    def setUp(self):
        self.app = ClothingSuggestionApp()

    def test_generate_dropdown(self):
        self.app.gender = input("Enter your gender (Male/Female): ")
        self.app.age = int(input("Enter your age: "))
        self.app.country = self.app.generate_dropdown(options=["Malaysia", "Indonesia", "Singapore", "Japan", "Korea", "Other"], prompt='Please select country')
        self.app.weather = self.app.generate_dropdown(options=["sunny", "cloudy", "rainy", "snowy", "windy", "other"], prompt='Please select weather')

    def test_suggest_clothes(self):
        self.app.gender = 'Male'
        self.app.age = 21
        self.app.country = 3
        self.app.weather = "sunny"
        self.app.suggest_clothes(self)

from Unittest import TestCase
from Test import ClothingSuggestionApp

class TestClothingSuggestionApp(TestCase):
    def setUp(self):
        self.app = ClothingSuggestionApp()

    def test_generate_dropdown(self):
        self.app.gender = input("Enter your gender (Male/Female): ")
        self.app.age = int(input("Enter your age: "))
        self.app.country = self.app.generate_dropdown(options=["Malaysia", "Indonesia", "Singapore", "Japan", "Korea", "Other"], prompt='Please select country')
        self.app.weather = self.app.generate_dropdown(options=["sunny", "cloudy", "rainy", "snowy", "windy", "other"], prompt='Please select weather')




