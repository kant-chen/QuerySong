# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('D:\\Coding\\Python\\py_folder\\qt_program\\qry_song\\firebase_db_key\\serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc = {
  'key': ["singer_id","song_name", "song_id" ],
  'value': ["辛曉琪","味道", 200564 ]
}

# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用

# 語法
# doc_ref = db.collection("集合名稱").document("文件id")

doc_ref = db.collection("sing_t　").document("song")

# doc_ref提供一個set的方法，input必須是dictionary

doc_ref.set(doc)
