import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import ListProperty, StringProperty

from db.bibledb import BibleDB

Builder.load_file('biblepage.kv')

class BibleVerse(BoxLayout):
    verse_num = StringProperty('')
    verse_txt = StringProperty('')

    def __init__(self, **kwargs):
        super(BibleVerse, self).__init__(**kwargs)
        print(str(kwargs))

class BiblePage(ScrollView):

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.find("")

    def find(self, condition):
        layout = BoxLayout(orientation='vertical')

        verse = BibleVerse(verse_num='1', verse_txt='a')
        layout.add_widget(verse)

        verse = BibleVerse(verse_num='2', verse_txt='b')
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