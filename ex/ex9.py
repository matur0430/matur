import requests
from bs4 import BeautifulSoup
url="https://www.melon.com/chart/index.htm"
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
response = requests.get(url,headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.select(".lst50")
print(response)
data=[]
print(result_list[0])
for res in result_list:
    r=res.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
    data.append(r.text)
print(data)
import csv
with open("melon.csv", mode="w", newline="\n", encoding='utf-8') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow([d])
