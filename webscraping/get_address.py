import requests
from bs4 import BeautifulSoup
import sqlite3

url_address=[]
#페이지 이동(분야별로 지정)#게임,연극,디자인,만화,예술,공예,사진,영화비디오,푸드,음악,테크,저널리즘,출판,
for i in range(1,21) :
    url = "https://kin.naver.com/userinfo/answerList.naver?u=NrYb6JQHc49tPAVE5lxSjaoFoSCEmqKU9dgbJ0pJP04%3D&year=2021&isWorry=false&page="+str(i)

#주소 저장하기
    res = requests.get(url)
    soup = BeautifulSoup(res.text , "html.parser")
    items = soup.find_all("td", attrs={"class":"title"})
    

#링크주소 리스트 만들기
    for item in items :
        link = item.find("a")['href']
        link = "https://kin.naver.com"+link
        url_address.append(link)

conn= sqlite3.connect("/Users/damon/project4/url_data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS ADDRESS;")

cur.execute("""CREATE TABLE ADDRESS (
    url VARCHAR NOT NULL PRIMARY KEY);""")

for url in url_address :
    url = url.replace('mydetail','detail')
    cur.execute("INSERT INTO ADDRESS (url) VALUES (?)", [url])
conn.commit()
