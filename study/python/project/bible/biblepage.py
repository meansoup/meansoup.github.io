import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import ListProperty, StringProperty

from search.biblesearchinfo import BibleSearchInfo
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

    def find(self, search):
        self.bible_info = BibleSearchInfo().to_bible_info(search)
        
        print(self.bible_info["book_name"])
        self.bible_title.title = self.bible_info["book_name"]
        self.make_layout()
        if self.bible_info['book_name'] == "검색":
            res = self.db.find_content(self.bible_info['content'])
            self.add_verse_list_with_book(res)
        else:
            res = self.db.find_chapter(self.bible_info['book'], self.bible_info['chapter'])
            self.add_verse_list(res)

    def add_verse_list_with_book(self, list):
        ex_words = ""
        colored_texts = [(text, self.markup_color_text("f08080", text)) for text in self.bible_info['content']]

        for verse in list:
            words = "%s %s" % (verse[0], verse[1])
            if ex_words != words:
                book_chapter = "%s %s장" % (BibleSearchInfo().get_bible_name(verse[0]), verse[1])
                colored_book_chapter = self.markup_color_text("87cefa", book_chapter)
                self.make_bible_verse("", colored_book_chapter)
                ex_words = words

            colored_verse = self.markup_color_texts(verse[3], colored_texts)
            self.make_bible_verse(str(verse[2]), colored_verse)

    def add_verse_list(self, list):
        for verse in list:
            self.make_bible_verse(str(verse[2]), verse[3])

    def markup_color_texts(self, verse, texts):
        for text in texts:
            verse = verse.replace(text[0], text[1])
        return verse

    def markup_color_text(self, color, text):
        return "[color=%s]%s[/color]" % (color, text)

    def make_bible_verse(self, number, content):
        self.layout.add_widget(Label(text=number, size_hint_x=.1))
        self.layout.add_widget(self.make_sized_label(content))

    def make_sized_label(self, content):
        label = Label(text=content, size_hint_y=None, markup=True)
        label.bind(width=lambda s, w: s.setter('text_size')(s, (w, None)))
        label.bind(texture_size=label.setter('size'))
        return label

    def calc_before_chapter(self):
        book = self.bible_info['book']
        chapter = self.bible_info['chapter']

        if chapter is 1:
            if book is 1:
                return "1 1"
            book = book - 1
            chapter = chapter_count[book]
        else:
            chapter = chapter - 1
        return "%s %s" % (book, chapter)

    def calc_next_chapter(self):
        book = self.bible_info['book']
        chapter = self.bible_info['chapter']

        if chapter is chapter_count[book]:
            if book is 66: # change constant name
                return "66 22"
            book = book + 1
            chapter = 1
        else:
            chapter = chapter + 1
        return "%s %s" % (book, chapter)

    def move_to(self, where):
        if self.bible_info['book_name'] == "검색":
            pass
        else:
            if where is "before":
                words = self.calc_before_chapter()
            elif where is "after":
                words = self.calc_next_chapter()
            self.find(words)

if __name__ == "__main__":
    print(chapter_count)
    aaa = {'a': 1, 'b': 2}
    print(aaa)
    aaa['a'] = 11111
    print(aaa)
