import requests
serviceKey='3q8gWw/OC7u5wDyD50CNAtEQ10QYLJMnWf70bBtxhsbm3cBtIPnoYEuwGn2BLfd2pC4EbNPMzOl3xzkM3shu5w=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey , 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
print(response.text)