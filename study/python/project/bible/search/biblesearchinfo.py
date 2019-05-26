import csv
import os
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bibleconstant import BibleConstant as C

class BibleSearchInfo:
    BOOK_FULL_NAME_FILE = 'bible_info.csv'
    BIBLE_BOOK_MAX_CNT = 66
    book_name = C.BookName.FULL

    def to_bible_info(self, words):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        os.chdir(BASE_DIR)

        book = self.bible_info_with_book(words) 
        if book is not False:
            chapter_verse = self.bible_info_with_chapter_verse(words)
            return {'book':book, 'chapter':chapter_verse[0]}
        else:
            pass
        # TODO:: make full search about input string.

        return {'book':'40', 'chapter':'1'}

    def bible_info_with_book(self, words):
        with open(self.BOOK_FULL_NAME_FILE, 'r', encoding='utf-8') as f:
            bible_info = list(csv.reader(f))

        for idx in range(len(bible_info)):
            if words.startswith(bible_info[idx][C.BookName.FULL.value]):
                print(str(bible_info[idx]) + " // " + str(C.BookName.FULL))
                self.book_name = C.BookName.FULL
                return idx + 1
        for idx in range(len(bible_info)):
            if words.startswith(bible_info[idx][C.BookName.SHORT.value]):
                print(str(bible_info[idx]) + " // " + str(C.BookName.SHORT))
                self.book_name = C.BookName.SHORT
                return idx + 1
        for idx in reversed(range(self.BIBLE_BOOK_MAX_CNT)):
            if words.startswith(str(idx + 1)):
                print(str(bible_info[idx]) + " // " + str(C.BookName.NUM))
                self.book_name = C.BookName.NUM
                return idx + 1

        return False
    
    def bible_info_with_chapter_verse(self, words):
        chapter_verse = re.findall("[0-9]+", words)
        n = len(chapter_verse)
        print(str(chapter_verse) + " // len: " + str(n))

        if n is 1:
            return (chapter_verse[0], 1)
        elif n is 2:
            if self.book_name is C.BookName.NUM:
                return (chapter_verse[1], 1)
            return chapter_verse
        elif n is 3:
            return (chapter_verse[1], chapter_verse[2])
        else:
            return (1, 1)

if __name__ == "__main__":
    own = BibleSearchInfo()
    own.to_bible_info("창세기 112 334")
    own.to_bible_info("창 112 ")
    own.to_bible_info("10 32 4")
    own.to_bible_info("1 32")
    own.to_bible_info("1 123 4")