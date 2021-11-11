import requests
from bs4 import BeautifulSoup
import sqlite3

#sqlite 데이터베이스에서 url 정보 불러오기
conn= sqlite3.connect("/Users/damon/project4/url_data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS dataset;")

#데이터 저장할 테이블 생성
cur.execute("""CREATE TABLE dataset (counseling VARCHAR)""")

url_list = cur.execute("""SELECT * FROM ADDRESS ORDER BY random()""")
url_address = url_list.fetchall()

#url정보 하나씩 접속해서 데이터 모으기
for item_url in url_address :
    print(item_url[0])
    res = requests.get(item_url[0])
    soup= BeautifulSoup(res.text ,"html.parser")
    items=soup.find_all("div", attrs={"class":"_endContentsText c-heading-answer__content-user"})
    for item in items :
        value = item.text
        cur.execute("INSERT INTO dataset (counseling) VALUES (?)", [value])
conn.commit()

