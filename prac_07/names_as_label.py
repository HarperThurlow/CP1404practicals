from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NamesAsLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["James", "Bob", "Jeff", "Billy"]

    def build(self):
        self.title = 'Names as labels'
        self.root = Builder.load_file('names_as_label.kv')
        self.print_names()
        return self.root

    def print_names(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)

            self.root.ids.names_box.add_widget(temp_label)


NamesAsLabels().run()
