from flask import Flask, Blueprint, render_template, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from datetime import datetime, timedelta
import os
import json
import sqlite3

app = Blueprint('main', __name__, url_prefix='/')
# 최초실행 : conn = sqlite3.connect('database.db')
# 최초실행 : conn.execute('create table stamp (pg text, tp text)')


# 0. sqlite DB 생성
# 1. flask web hosting - git, pythonanywhere 이용
# 2. 호출 html에 링크 삽입
# 3. template html img 파일 경로 구현

## 해보고 안되면 form에 변수 0/1 추가(버튼클릭여부), 페이지 호출 always form submit, if문으로 구분하도록 코드 수정

# page 호출 때 data 가져옴
@app.route('/')
def index():
    #구현: pg 가져오기
    pg = '0'
    tp = 'none'
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("select * from stamp where pg = '" + pg + "'")
        if len(cur) == 0:
            cur.execute("insert into stamp values('" + pg + "', 'none')")
        else:
            tp = cur[0][1] # 맞는지 확인
        cur.close()
    return render_template('/main/index.html', tp = tp)


# button 클릭했을 때 data 변경/갱신
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        #구현: post로 가져온 변수값 초기화
        pg = request.form['pg']
        tp = request.form['tp']
        
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("update stamp set tp = '" + tp + "' where pg = '" + pg + "'")
            cur.close()
        return render_template('/main/index.html', tp = tp);




# app = Flask(__name__)
# 
# @app.route('/')
# @app.route('/home')
# def home():
    # return('home')