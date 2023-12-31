from PIL import Image
import os
import requests


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
        return resized_filename

    def get_user_input(self):
        self.gender = input("Enter your gender (Male/Female): ")
        self.age = int(input("Enter your age: "))
        countries = ["Indonesia", "Singapore", "North Korea", "Japan", "Malaysia", "Other"]
        self.country = self.generate_dropdown(countries, "Select your country:")

        # Use the requests API to fetch weather data
        try:
            response = requests.get("https://openweathermap.org/api")
            weather_data = response.json()
            self.weather = weather_data.get("weather", "other")
        except Exception as e:
            print(f"Error fetching weather data: {str(e)}")
            self.weather = "other"

    def suggest_clothes(self):
        suggestion = ""

        if self.gender.lower() == "male":
            suggestion += "man " if self.age > 18 else "boys "
        elif self.gender.lower() == "female":
            suggestion += "woman " if self.age > 18 else "girls "


        weather_options = {
            "sunny": ("shorts and t-shirt", "sunny.jpg", (400, 600)),
            "cloudy": ("denim jacket and pants", "cloudy.jpg", (400, 600)),
            "rainy": ("raincoat and umbrella", "rainy.jpg", (400, 600)),
            "snowy": ("waterproof insulated jackets and pants", "snowy.jpg", (400, 600)),
            "windy": ("windproof hoodie and jean pants", "windy.jpg", (400, 600)),
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
        print(f"Resized Image: {self.image}")


if __name__ == "__main__":
    while True:
        app = ClothingSuggestionApp()
        app.get_user_input()
        suggested_clothes = app.suggest_clothes()
        app.display_suggestion(suggested_clothes)

        repeat = input("Do you want to get another clothing suggestion? (yes/no): ").lower()
        if repeat != "yes":
            break
