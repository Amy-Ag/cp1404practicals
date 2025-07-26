from kivy.app import App
from kivy.app import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build kivy GUI and load the kivy file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Handle and update the greet button accordingly."""
        print("Greet")
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"
    def handle_clear(self):
        """Clear and reset the input field."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
