import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from db.bibledb import BibleDB
from bibleverse import BibleVerse

Builder.load_file('bibleverse.kv')
Builder.load_file('bibleverselist.kv')

class BiblePage(FloatLayout):
    page_num = 0
    verse_num = 0

    def __init__(self):
        pass
        self.find("")

    def find(self, condition):
        db = BibleDB()
        res = db.find(condition)
        
        # print(res)
    
    #     for verse in res:
    #         self.add_verse(verse[2], verse[3])

    # def add_verse(self, num, txt):
    #     list = self.bible_verse_list
    #     verse = BibleVerse(num, txt)

    #     list.add_widget(verse)

class BiblePageApp(App):
    def build(self):
        return BiblePage()

if __name__ == "__main__":
    BiblePageApp().run()