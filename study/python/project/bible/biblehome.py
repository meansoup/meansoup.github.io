import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from biblepage import BiblePage

class BibleHome(FloatLayout):
    pass

class BibleHomeApp(App):
    def build(self):
        return BibleHome()

if __name__ == "__main__":
    BibleHomeApp().run()
