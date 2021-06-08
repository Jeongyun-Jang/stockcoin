from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
@app.route('/')
def home():
   return render_template('index.html')
'''
@app.route('/review', methods=['POST'])
def write_review1():
    title_receive = request.form['title_give']
    doc = {
        'title': title_receive,
    }
    print(title_receive)
    write_review1.title = title_receive
    return jsonify({'msg': '앱 검색 완료!'})
'''
@app.route('/review', methods=['GET'])
def read_reviews1():
    title_receive = request.args.get('title_give')
    print(title_receive)
    reviews = list(db.review.find({'title': title_receive}, {'_id': False}))
#    reviews = list(db.review.find({'appname': title_receive },{'_id': False}))

    print(reviews)
    return jsonify({'all_reviews': reviews})
## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    appname_receive = request.form['appname_give']
    comment_receive = request.form['comment_give']
    star1_receive = request.form['star1_give']
    star2_receive = request.form['star2_give']
    star3_receive = request.form['star3_give']
    star4_receive = request.form['star4_give']
    doc={
        'appname': appname_receive,
        'comment': comment_receive,
        'star1': star1_receive,
        'star2': star2_receive,
        'star3': star3_receive,
        'star4': star4_receive
    }
    db.review.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

'''

@app.route('/review', methods=['GET'])
def read_reviews1():
    title_receive = request.args.get('title_give')
    title_receive = str(title_receive)
    print(title_receive)
    reviews = list(db.review.find({'comment': title_receive },{'_id': False}))
    print(reviews) # 같은 appname 값을 안가져옴
    return jsonify({'all_reviews': reviews})

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    appname_receive = request.form['appname_give']
    comment_receive = request.form['comment_give']
    star1_receive = request.form['star1_give']
    star2_receive = request.form['star2_give']
    star3_receive = request.form['star3_give']
    star4_receive = request.form['star4_give']

    doc={
        'appname': appname_receive,
        'comment': comment_receive,
        'star1': star1_receive,
        'star2': star2_receive,
        'star3': star3_receive,
        'star4': star4_receive

    }
    db.review.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
'''