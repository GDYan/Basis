import requests
from bs4 import BeautifulSoup
import re
import lxml

def yahoo_message():
    # 下載 Yahoo 首頁內容
    r = requests.get('https://tw.yahoo.com/')

    # 確認是否下載成功
    if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')

        # 以 CSS 的 class 抓出各類頭條新聞
        stories = soup.find_all('a', class_='story-title')
        for s in stories:
            # 新聞標題
            print("標題：" + s.text)
            # 新聞網址
            print("網址：" + s.get('href'))

def doubanfordan():
    s = 0
    r = requests.get('https://book.douban.com/subject/34691868/?icn=index-latestbook-subject')
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        pattern = soup.find_all('span', 'short')
        print("pattern=", pattern)
        for iterm in pattern:
            print(iterm.string)
        pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')
        p = re.findall(pattern_s, r.text)
        print(p)
        for star in p:
            s += int(star)
        print("result =")
    else:
        print("failed")

if __name__ == "__main__" :
    yahoo_message()
    doubanfordan()
