import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from biblepage import BiblePage
from search.biblesearchinfo import BibleSearchInfo

Builder.load_file('font/font.kv')
Builder.load_file('widget/actionitems.kv')
Builder.load_file('widget/floatbutton.kv')

# action bar
# 현재 보는 말씀 ex. 창 1.1

class BibleHome(FloatLayout):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.search("1 1")

    def search(self, words):
        bible_info = BibleSearchInfo().to_bible_info(words)
        self.bible_page.find(bible_info)
        self.bible_title.title = bible_info["book_name"]

class BibleHomeApp(App):
    def build(self):
        return BibleHome()

if __name__ == "__main__":
    BibleHomeApp().run()