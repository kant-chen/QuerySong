# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate("D:\\Coding\\Python\\py_folder\\qt_program\\qry_song\\firebase_db_key\\serviceAccount.json")


# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc = {
    'song001': 2,
    'song002': "abcd"
}

# 語法
# collection_ref = db.collection("集合路徑")

collection_ref = db.collection("song")
