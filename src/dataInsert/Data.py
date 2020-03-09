import pymysql.cursors
from General.Pair import Pair


class Data:

    def __init__(self):
        self.config = \
            {
                "host": "localhost",
                "user": "11510700",
                "password": "160877",
                "database": "Graduation"
            }
        self.db = pymysql.connect(**self.config)
        self.cursor = self.db.cursor()

    def insert_sentence(self, original_sentence):
        sql = "INSERT INTO sentences VALUES(null,"
        self.cursor.execute(sql + "'" + original_sentence + "',NULL)")
        self.db.commit()

    def insert_sentences(self, original_sentence, mutated_sentence):
        sql = "SELECT sentence_id, original_sentence FROM sentences;"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        for data in datas:
            if original_sentence in data:
                sentence_id = str(data[0])
                sql = \
                    "UPDATE sentences SET mutation_sentence='" \
                    + mutated_sentence + \
                    "' WHERE sentence_id=" \
                    + sentence_id
                self.cursor.execute(sql)
                self.db.commit()
                return
        sql = "INSERT INTO sentences VALUES(null,"
        self.cursor.execute(sql + "'" + original_sentence + "','" + mutated_sentence + "')")
        self.db.commit()

    def get_sentence(self):
        sql = "SELECT original_sentence, mutation_sentence FROM graduation.sentences;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        all_pairs = []
        for p in data:
            pair = Pair(p[0])
            if p[1] is not None:
                pair.set_mutation(p[1])
            all_pairs.extend(pair)
        return all_pairs

    def close(self):
        self.cursor.close()
        self.db.close()
