import sqlite3
import os

class BibleDB():
    conn = None
    conn_open = False

    def find_chapter(self, book, chapter):
        if self.conn_open is False:    
            BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
            os.chdir(BASE_DIR)
            self.conn = sqlite3.connect('bible.sqlite3')
            self.conn_open = True

        cur = self.conn.cursor()
        query = "select * from bibleKorHRV where book = {0} and chapter = {1}".format(book, chapter)
        cur.execute(query)

        res = cur.fetchall()
        self.conn.close()
        self.conn_open = False
        
        return res