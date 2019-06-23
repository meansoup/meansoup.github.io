import sqlite3
import os

class BibleDB():
    conn = None
    conn_open = False
    cur = None
    language = "bibleKorHRV"

    def connect(self):
        if self.conn_open is False:    
            BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
            os.chdir(BASE_DIR)
            self.conn = sqlite3.connect('bible.sqlite3')
            self.conn_open = True
            self.cur = self.conn.cursor()

    def find_chapter(self, book, chapter):
        self.connect()

        query = "select * from " + self.language + " where book = {0} and chapter = {1}".format(book, chapter)
        self.cur.execute(query)

        res = self.cur.fetchall()
        
        self.conn.close()
        self.conn_open = False
        
        return res

    def find_content(self, words):
        self.connect()

        query = "select * from bibleKorHRV where"
        for word in words:
            query = query + " content like '%" + word + "%' and"
        query = query[:-4]

        self.cur.execute(query)

        res = self.cur.fetchall()

        self.conn.close()
        self.conn_open = False
        
        return res

class EngBibleDB(BibleDB):
    language = "bibleEngKJV"

if __name__ == "__main__":
    db = BibleDB()
    res = db.find_content(["여호와", "하나님"])

    cnt = 0
    for con in res:
        cnt = cnt + 1
    print(str(cnt))