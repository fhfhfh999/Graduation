import pymysql.cursors

from General.Pair import Pair

sql = "SELECT * FROM graduation.sentences;"
config = {"host": "localhost",
          "user": "11510700",
          "password": "160877",
          "database": "Graduation"
          }
db = pymysql.connect(**config)
cursor = db.cursor()
cursor.execute(sql)
data = cursor.fetchall()
for p in data:
    pair = Pair(p[0])
    if p[1] is not None:
        pair.set_mutation(p[1])
    # TODO: send the pair to the place needed
