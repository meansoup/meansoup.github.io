import kivy
kivy.require('1.9.0')

from kivy.uix.relativelayout import RelativeLayout

class BibleVerse(RelativeLayout):
    num = 0
    txt = ""

    def __init__(self, num, txt):
        self.num = num
        self.txt = txt