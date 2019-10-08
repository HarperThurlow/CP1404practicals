from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesToKilometerApp(App):

    def build(self):
        self.title = "Converting Miles to Kilometers with Kivy"
        self.root = Builder.load_file('new_convert_m_to_km.kv')
        return self.root

    def convert_calc(self):
        value = self.handle_valid_input()
        result = value * CONVERSION
        self.root.ids.output_value.text = str(result)

    def handle_increment(self, change):

        value = self.handle_valid_input() + change
        self.root.ids.input_number.text = str(value)

    def handle_valid_input(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0


MilesToKilometerApp().run()
