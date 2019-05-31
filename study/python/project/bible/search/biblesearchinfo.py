import csv
import os
import re
import sys
from enum import Enum

BOOK_FULL_NAME_FILE = 'bible_info.csv'
BIBLE_BOOK_MAX_CNT = 66

class BookName(Enum):
    FULL = 0
    SHORT = 1
    NUM = 2

class BibleSearchInfo:
    book_name = BookName.FULL

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        os.chdir(BASE_DIR)
        with open(BOOK_FULL_NAME_FILE, 'r', encoding='utf-8') as f:
            self.bible_info = list(csv.reader(f))

    def to_bible_info(self, words):
        book = self.bible_info_with_book(words) 
        if book is not False:
            chapter_verse = self.bible_info_with_chapter_verse(words)
            if chapter_verse is False:
                # TODO:: make bible name with full search.
                pass
            else:
                return {'book_name':self.get_bible_name(book), 'book':book, 'chapter':chapter_verse[0]}
        else:
            # TODO:: make full search about input string.
            pass

        return {'book':'40', 'chapter':'1'}

    def bible_info_with_book(self, words):
        for idx in range(BIBLE_BOOK_MAX_CNT):
            if words.startswith(self.bible_info[idx][BookName.FULL.value]):
                print(str(self.bible_info[idx]) + " // " + str(BookName.FULL))
                self.book_name = BookName.FULL
                return idx + 1

        for idx in range(BIBLE_BOOK_MAX_CNT):
            if words.startswith(self.bible_info[idx][BookName.SHORT.value]):
                print(str(self.bible_info[idx]) + " // " + str(BookName.SHORT))
                self.book_name = BookName.SHORT
                return idx + 1
                
        for idx in reversed(range(BIBLE_BOOK_MAX_CNT)):
            if words.startswith(str(idx + 1)):
                print(str(self.bible_info[idx]) + " // " + str(BookName.NUM))
                self.book_name = BookName.NUM
                return idx + 1

        return False
    
    def bible_info_with_chapter_verse(self, words):
        chapter_verse = re.findall("[0-9]+", words)
        n = len(chapter_verse)
        print(str(chapter_verse) + " // len: " + str(n))

        if n is 0:
            return False
        elif n is 1:
            return (chapter_verse[0], 1)
        elif n is 2:
            if self.book_name is BookName.NUM:
                return (chapter_verse[1], 1)
            return chapter_verse
        elif n is 3:
            return (chapter_verse[1], chapter_verse[2])
        else:
            if self.book_name is BookName.NUM:
                return (chapter_verse[1], chapter_verse[2])
            else:
                return (chapter_verse[0], chapter_verse[1])

    def get_bible_name(self, book):
        idx = book - 1
        full_name = self.bible_info[idx][BookName.FULL.value]
        return full_name


if __name__ == "__main__":
    own = BibleSearchInfo()
    own.to_bible_info("창세기 112 334")
    own.to_bible_info("창 112 ")
    own.to_bible_info("10 32 4")
    own.to_bible_info("66 1 4")
    own.to_bible_info("40 13 4")
    own.to_bible_info("1 32")