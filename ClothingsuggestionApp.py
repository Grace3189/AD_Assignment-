from PIL import Image
import os

class ClothingSuggestionApp:
    def __init__(self):
        self.gender = None
        self.age = None
        self.country = None
        self.weather = None
        self.image = None

    @staticmethod
    def generate_dropdown(options, prompt):
        print(prompt)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        selected_index = int(input(f"Enter the number corresponding to your choice (1-{len(options)}): "))
        selected_option = options[selected_index - 1]

        return selected_option

    @staticmethod
    def open_resize_image(original_image_file_path, new_size):
        image = Image.open(original_image_file_path)
        filename, extension = os.path.splitext(os.path.basename(original_image_file_path))
        resized_filename = f"{filename}_resized{extension}"
        resized_image = image.resize(new_size)
        resized_image.save(resized_filename)
        resized_image.show()

    def get_user_input(self):
        self.gender = input("Enter your gender (Male/Female): ")
        self.age = int(input("Enter your age: "))
        countries = ["Malaysia", "Indonesia", "Singapore", "Japan", "Korea", "Other"]
        self.country = self.generate_dropdown(countries, "Select your country:")
        weathers = ["sunny", "cloudy", "rainy", "snowy", "windy", "other"]
        self.weather = self.generate_dropdown(weathers, "Select your current weather:")

    def suggest_clothes(self):
        suggestion = ""

        if self.gender.lower() == "male":
            suggestion += "man " if self.age > 18 else "boys "
        elif self.gender.lower() == "female":
            suggestion += "woman " if self.age > 18 else "girls "

        weather_options = {
            "sunny": ("short and t-shirt", "sunny.jpg", (400, 600)),
            "cloudy": ("light jacket and pant", "cloudy.jpg", (400, 600)),
            "rainy": ("water proof jacket and pant", "rainy.jpg", (400, 600)),
            "snowy": ("winter insulated jacket and pant", "snowy.jpg", (400, 600)),
            "windy": ("windproof jacket and pants", "windy.jpg", (400, 600)),
            "other": ("business casual", "business_casual.jpg", (400, 600)),
        }

        selected_weather = self.weather.lower()
        suggestion += weather_options.get(selected_weather, weather_options["other"])[0]

        original_image_file_path = weather_options[selected_weather][1]
        new_size = weather_options[selected_weather][2]
        self.image = self.open_resize_image(original_image_file_path, new_size)

        return suggestion

    def display_suggestion(self, suggestion):
        print(f"Based on the information you provided, we suggest '{suggestion}', considering your preferences.")

if __name__ == "__main__":
    app = ClothingSuggestionApp()
    app.get_user_input()
    suggested_clothes = app.suggest_clothes()
    app.display_suggestion(suggested_clothes)