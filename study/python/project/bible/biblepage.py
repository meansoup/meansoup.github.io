import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

from db.bibledb import BibleDB
from bibleverse import BibleVerse

# Builder.load_file('biblepage.kv')
Builder.load_file('bibleverse.kv')
Builder.load_file('bibleverselist.kv')

class BiblePage(ScrollView):
    page_num = 0
    verse_num = 0

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.find("")

    def find(self, condition):
        layout = BoxLayout(orientation='vertical')

        bt = Button(text='hello world', font_size=10)
        layout.add_widget(bt)
        verse = BibleVerse("1", "aaaaa")
        layout.add_widget(verse)

        self.add_widget(layout)

        # db = BibleDB()
        # res = db.find(condition)gcgvg
        
        # print(res)
    
        # for verse in res:
        #     self.add_verse(verse[2], verse[3])

    def add_verse(self, num, txt):
        list = self.bible_verse_list
        verse = BibleVerse(num, txt)

        list.add_widget(verse)