import firebase_admin 
from firebase_admin import credentials, firestore

from register import db

def item_buy(user,item):
  db.collection("User").document(user).update({"item":firestore.ArrayUnion([item])})

def item_buyList_get(user):
  itemList=db.collection("User").document(user).get().to_dict()
  return itemList["item"]

def item_apply(user,item):
  db.collection("User").document(user).update({"item_apply":item})


def item_apply_get(user):
  field=db.collection("User").document(user).get().to_dict()
  return field["item_apply"]



list=item_buyList_get("gajigaji1212@naver.com")
print(list)