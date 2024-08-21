import csv
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}


res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
# res = requests.get('https://www.melon.com/chart/index.htm')#에러
# print(res.status_code)#406에러  헤더값 추가하여 해결
soup = BeautifulSoup(res.text, 'html.parser')
songs = soup.select('.lst50,.lst100')  # 개발자도구에서 요소에서 검사 선택
print(len(songs))
# print(songs[0])
melon_list = []
for song in songs:
    tmp = []
    tmp.append(song.select_one('.rank').text)
    tmp.append(song.select_one('.ellipsis.rank01').text.replace('\n', ""))
    tmp.append(song.select_one('.ellipsis.rank02').a.text.replace('\n', ""))
    melon_list.append(tmp)
print(melon_list)

