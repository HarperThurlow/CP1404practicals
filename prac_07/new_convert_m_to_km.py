from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesToKilometerApp(App):

    def build(self):
        self.title = "Converting Miles to Kilometers with Kivy"
        self.root = Builder.load_file('new_convert_m_to_km.kv')
        return self.root

    def convert_calc(self):
        value = float(self.root.ids.input_number.text)
        result = value * CONVERSION
        self.root.ids.output_value.text = str(result)

    def handle_increment(self, change):

        value = float(self.root.ids.input_number.text) + change
        self.root.ids.input_number.text = str(value)


MilesToKilometerApp().run()
