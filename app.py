from flask import url_for, session, Flask, render_template, request,redirect, jsonify
import hashlib
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.amsx0.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.timeattack


app = Flask(__name__)


@app.route('/api/signup', methods=['POST'])
def SignUpReceive():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_receive = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'user_id': id_receive,
        'user_pw': pw_receive
    }

    id = db.users.find_one({"user_id": id_receive})
    if id == None:
        pass
    else:
        return jsonify({'result': 'fail', 'msg': '중복된 아이디입니다!'})
    if not (id_receive and pw_receive):
        return jsonify({'result': 'fail', 'msg': '모두 입력해주세요!'})

    else:
        db.users.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '회원가입 되었습니다!'})

app.run(host="0.0.0.0")


