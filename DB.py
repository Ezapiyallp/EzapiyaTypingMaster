import sqlite3


class DB:
    def __init__(self):
        self.db = sqlite3.connect('Typing_Data.db')

    def runSql(self, sql):
        self.db.execute(sql)
        self.db.commit()

    def runSelect(self, sql):
        cur = self.db.cursor()
        cur.execute(sql)
        return cur

