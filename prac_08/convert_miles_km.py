"""
CP1404/CP5632 Practical
Kivy GUI program about MilesConverterApp
"""
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres"""
    output_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation and update output"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press and update values"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Validate and return miles input as float, return 0 if invalid"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()