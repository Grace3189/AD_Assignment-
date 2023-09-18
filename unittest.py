from unittest import TestCase
from clothingsuggestion import ClothingSuggestionApp

class TestClothingSuggestionApp(unittest.TestCase):

    def test_generate_dropdown(self):
        app = ClothingSuggestionApp()
        options = ["Option 1", "Option 2", "Option 3"]
        prompt = "Select an option:"

        # Mock the input function to return a fixed value
        input_mock = lambda _: "2"
        original_input = __builtins__.input
        __builtins__.input = input_mock

        selected_option = app.generate_dropdown(options, prompt)

        # Restore the original input function
        __builtins__.input = original_input

        self.assertEqual(selected_option, "Option 2")

    def test_open_resize_image(self):
        app = ClothingSuggestionApp()
        original_image_file_path = "path/to/original_image.jpg"
        new_size = (100, 100)

        resized_filename = app.open_resize_image(original_image_file_path, new_size)
        resized_image = Image.open(resized_filename)

        self.assertEqual(resized_image.size, new_size)

        # Clean up the resized image file
        os.remove(resized_filename)

if __name__ == "__main__":
    unittest.main()