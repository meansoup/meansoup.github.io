# File name: widgets2.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class WidgetsApp(App):
    def build(self):
        return MyWidget()

if __name__=="__main__":
    WidgetsApp().run()
