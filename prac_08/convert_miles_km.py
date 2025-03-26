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
        result = float(input_mile) * KM_PER_MILE
        self.output_message = str(result)

    def handle_increment(self,input_mile, increment):
        updated_mile = float(input_mile) + increment
        self.root.ids.input_mile.text = str(updated_mile)
        self.handle_convert(updated_mile)

ConvertMilesToKM().run()