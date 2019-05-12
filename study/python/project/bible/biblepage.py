import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.properties import ListProperty, StringProperty

from db.bibledb import BibleDB

Builder.load_file('biblepage.kv')

# https://stackoverflow.com/questions/46324709/kivy-label-multiline-text

class BibleVerse(GridLayout):
    verse_number = StringProperty('')
    verse_content = StringProperty('')

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

class BiblePage(ScrollView):
    layout = None
    db = None

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1, spacing=30, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.db = BibleDB()

        self.find("")

    def find(self, condition):
        self.add_widget(self.layout)

        verse_str = "1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnm"
        
        bible_verse = BibleVerse(verse_number=str("abc"), verse_content=verse_str, size_hint_y=.3)
        self.layout.add_widget(bible_verse)

        bible_verse = BibleVerse(verse_number=str("abc"), verse_content=verse_str, size_hint_y=.3)
        self.layout.add_widget(bible_verse)

        res = self.db.find_chapter("1", "1")
        self.add_verse_list(res)

    def add_verse_list(self, list):
        for verse in list:
            bible_verse = BibleVerse(verse_number=str(verse[2]), verse_content=verse[3])
            self.layout.add_widget(bible_verse)