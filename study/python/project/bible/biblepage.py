import kivy
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import ListProperty, StringProperty

from search.biblesearchinfo import BibleSearchInfo
from bibleconstants import *
from db.bibledb import BibleDB
from db.bibledb import EngBibleDB
from widget.endeventscroll import EndEventScroll
from widget.verse import VerseLabel
from widget.verse import VerseTitle


class BiblePage(EndEventScroll):
    layout = None
    layout_exist = False
    db = None
    edb = None
    verse_list_search = None
    verse_cnt = 0
    height_changed_cnt = 0
    ex_height = 0

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.db = BibleDB()
        self.edb = EngBibleDB()

    def on_end_event(self):
        if self.bible_info['book_name'] == "검색":
            ex_height = self.layout.height
            self.add_verse_list_search()

    def make_layout(self):
        if self.layout_exist is True:
            self.remove_widget(self.layout)

        self.layout_exist = True
        self.layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.layout.bind(height=self.height_changed)
        self.add_widget(self.layout)

    def find(self, search):
        self.ex_height = 0
        self.bible_info = BibleSearchInfo().to_bible_info(search)
        
        print(self.bible_info["book_name"])
        self.make_layout()
        if self.bible_info['book_name'] == "검색":
            res = self.db.find_content(self.bible_info['content'])
            self.bible_title.title = "%s %s" % (self.bible_info["book_name"], str(len(res)))
            self.verse_list_search = self.add_verse_list_search_generator(res)
            self.add_verse_list_search()
        else:
            self.bible_title.title = "%s %s" % (self.bible_info["book_name"], self.bible_info["chapter"])
            res = self.db.find_chapter(self.bible_info['book'], self.bible_info['chapter'])
            eng_res = self.edb.find_chapter(self.bible_info['book'], self.bible_info['chapter'])
            self.add_verse_list(res, eng_res)

    def add_verse_list_search(self):
        try:
            next(self.verse_list_search)
        except StopIteration:
            pass

    def add_verse_list_search_generator(self, list):
        ex_words = ""
        colored_texts = [(text, "[color=f08080]%s[/color]" % text) for text in self.bible_info['content']]
        self.verse_cnt = 0

        for verse_info in list:
            self.height_changed_cnt = 0
            words = "%s %s" % (verse_info[0], verse_info[1])
            self.verse_cnt += 1
            if ex_words != words:
                book_chapter = "%s %s장" % (BibleSearchInfo().get_bible_name(verse_info[0]), verse_info[1])
                verse_title = VerseTitle(text=book_chapter, size_hint_y=None)
                self.layout.add_widget(verse_title)
                ex_words = words

            verse_info_list = [item for item in verse_info]
            verse_info_list[3] = self.markup_color_texts(verse_info[3], colored_texts)
            verse = VerseLabel(info_list=verse_info_list, is_search=True, size_hint_y=None)
            # verse.bind(height=self.verse_height_changed)
            self.layout.add_widget(verse)

            if self.verse_cnt % 50 == 0:
                yield

    def height_changed(self, *args):
        self.height_changed_cnt += 1
        # print("[" + str(self.height_changed_cnt) + "] !!height Changed: " + str(args[1]))

        if self.height_changed_cnt is 3: # first - added, second - strange, third - real value.
            print("ex: " + str(self.ex_height) + " cur: " + str(args[1]))
            percent = self.ex_height / args[1]
            self.scroll_y = 1 - percent
            self.ex_height = args[1]

    # def verse_height_changed(self, *args):
    #     verse_id = str(args[0])[-8:-1]
    #     # self.verse_height[verse_id] = args[1]
    #     if verse_id in self.temp_verse_height:
    #         print("**")
    #         self.verse_height[verse_id] = args[1]
    #     else: 
    #         print("@")
    #         self.temp_verse_height[verse_id] = None

    #     # 어차피 verse_height는 비동기적으로 업데이트 되서 더 느리게 되니까
    #     # verse_cnt가 50인지, 끝까지 왔는지를 확인하지 않아도 됨.
    #     changed_length = len(self.verse_height)
    #     if changed_length is self.verse_cnt:
    #         print("E")
    #         print(str(self.verse_height))
    #         print("sum: " + str(sum(self.verse_height.values())))

    def add_verse_list(self, list, eng_list):
        for i in range(len(list)):
            verse = VerseLabel(info_list=list[i], eng_content=eng_list[i][3], size_hint_y=None)
            self.layout.add_widget(verse)

    def markup_color_texts(self, verse, texts):
        for text in texts:
            verse = verse.replace(text[0], text[1])
        return verse

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
