import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout


# Create the widget class
class textinp(Widget):
    pass


# Create the app class
class MainApp(App):

    # Building text input
    def build(self):
        self.title = 'Harpocrates Client'
        return textinp()

    # Arranging that what you write will be shown to you
    # in IDLE
    def process(self):
        text = self.root.ids.input.text
        # print(text)


# Run the App
if __name__ == "__main__":
    MainApp().run()
