from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.60934

class ConvertMilesToKM(App):
    output_message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self,input_mile):
        input_mile = self.get_valid_input_mile(input_mile)
        result = input_mile * KM_PER_MILE
        self.output_message = str(result)

    def handle_increment(self,input_mile, increment):
        input_mile = self.get_valid_input_mile(input_mile)
        updated_mile = input_mile + increment
        self.root.ids.input_mile.text = str(updated_mile)
        self.handle_convert(updated_mile)

    @staticmethod
    def get_valid_input_mile(input_mile):
        try:
            input_mile = float(input_mile)
        except ValueError:
            input_mile = 0
        return input_mile

ConvertMilesToKM().run()