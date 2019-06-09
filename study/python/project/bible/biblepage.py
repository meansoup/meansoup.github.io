import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import ListProperty, StringProperty

from bibleconstants import *
from db.bibledb import BibleDB

class BiblePage(ScrollView):
    layout = None
    layout_exist = False
    db = None
    old_book_info = None

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.db = BibleDB()

    def make_layout(self):
        if self.layout_exist is True:
            self.remove_widget(self.layout)

        self.layout_exist = True
        self.layout = GridLayout(cols=2, size_hint_y=None, spacing=10)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.add_widget(self.layout)

    def find(self, book_info):
        self.old_book_info = book_info
        self.make_layout()
        if book_info['book_name'] is "검색":
            res = self.db.find_content(book_info['content'])
        else:
            res = self.db.find_chapter(book_info['book'], book_info['chapter'])
        
        self.add_verse_list(res)

    def add_verse_list(self, list):
        for verse in list:
            self.make_bible_verse(str(verse[2]), verse[3])

    def make_bible_verse(self, number, content):
        self.layout.add_widget(Label(text=number, size_hint_x=.1))
        self.layout.add_widget(self.make_sized_label(content))

    def make_sized_label(self, content):
        label = Label(text=content, size_hint_y=None)
        label.bind(width=lambda s, w: s.setter('text_size')(s, (w, None)))
        label.bind(texture_size=label.setter('size'))
        return label

    def calc_before_chapter(self):
        book = self.old_book_info['book']
        chapter = self.old_book_info['chapter']

        if chapter is 1:
            if book is 1:
                return
            print("calccccc")
            self.old_book_info['book'] = book - 1
            self.old_book_info['chapter'] = chapter_count[book]
        else:
            self.old_book_info['chapter'] = chapter - 1

    def move_to_before(self):
        if self.old_book_info['book_name'] is "검색":
            pass
        else:
            self.calc_before_chapter()
            self.find(self.old_book_info)
            print("before!!!!")

    def move_to_next(self):
        print("next!!!!")

if __name__ == "__main__":
    print(chapter_count)
    aaa = {'a': 1, 'b': 2}
    print(aaa)
    aaa['a'] = 11111
    print(aaa)
