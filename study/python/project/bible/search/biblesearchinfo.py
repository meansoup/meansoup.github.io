import csv
import os

class BibleSearchInfo:
    BOOK_FULL_NAME = 'bible_info.list'

    def to_bible_info(self, words):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        os.chdir(BASE_DIR)

        # TODO:: make book check method include this... make chapter check also.
        book = self.bible_info_with_book(words) 
        if book is not False:
            return {'book':book, 'chapter':'1'}

        return {'book':'40', 'chapter':'1'}

    def bible_info_with_book(self, words):
        with open(self.BOOK_FULL_NAME, 'r', encoding='utf-8') as f:
            bible_info = f.read().splitlines()

        for idx in range(len(bible_info)):
            book = bible_info[idx]
            if words.startswith(book):
                print(str("**" + book + " " + str(idx) + "..."))
                return idx + 1

        return False