from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.dbsparta

db.cardview.drop()
doc = {
        'appname': "Win.k",
        'img_url': "https://is5-ssl.mzstatic.com/image/thumb/Purple124/v4/79/43/fd/7943fdcc-51cd-0d38-560d-1f63da6f45b7/source/512x512bb.jpg",
        'company': '교보증권',
        'app_url': 'https://play.google.com/store/apps/details?id=kr.com.wink&hl=ko&gl=US',
    }

db.cardview.insert_one(doc)

db.review.drop()


doc = {
    "title" : "Win.k",
    "comment" : "코멘트",
    "star1" : "1",
    "star2" : "2",
    "star3" : "3",
    "star4" : "4"
}

db.review.insert_one(doc)

