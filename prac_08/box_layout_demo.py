"""
CP1404/CP5632 Practical
Kivy GUI program about BoxLayoutDemo
"""
from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """SquareNumberApp is a Kivy App for create and manage a presentation application based on Box layout."""
    def build(self):
        """Set application title and load KV file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print test information."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the input box content."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"

BoxLayoutDemo().run()