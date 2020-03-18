import pymysql.cursors
import os

config = {"host": "localhost",
          "user": "11510700",
          "password": "160877",
          "database": "Graduation"}


db = pymysql.connect(**config)
cursor = db.cursor()


def insert_sentence(original_sentence):
    sql = "INSERT INTO sentences VALUES(null,"
    cursor.execute(sql + "'" + original_sentence + "',NULL)")
    db.commit()


def insert_sentences(original_sentence, mutated_sentence):
    sql = "SELECT sentence_id, original_sentence FROM sentences;"
    cursor.execute(sql)
    datas = cursor.fetchall()
    for data in datas:
        if original_sentence in data:
            sentence_id = str(data[0])
            sql = \
                "UPDATE sentences SET mutation_sentence='"\
                + mutated_sentence + \
                "' WHERE sentence_id="\
                + sentence_id
            cursor.execute(sql)
            db.commit()
            return
    sql = "INSERT INTO sentences VALUES(null,"
    cursor.execute(sql + "'" + original_sentence + "','" + mutated_sentence + "')")
    db.commit()


# TODO（shf):  use the method upside to insert the sentence into database

# file = open("C:\\Users\\77291\\Documents\\python\\Graduation\\res\\cn.txt", encoding="UTF-8")
# all_lines = file.readlines()
# for line in all_lines:
#     line = "".join(line.split())
#     print(line)
#     insert_sentence(line)
# file.close()

# test_data1 = "今天天气真好"
# test_data2 = "今天的天气真好"
# insert_sentences(test_data1, test_data2)

cursor.close()
db.close()

