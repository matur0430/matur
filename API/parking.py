import requests
serviceKey='3q8gWw/OC7u5wDyD50CNAtEQ10QYLJMnWf70bBtxhsbm3cBtIPnoYEuwGn2BLfd2pC4EbNPMzOl3xzkM3shu5w=='
url = 'http://apis.data.go.kr/B551177/StatusOfParking/getTrackingParking'
params ={'serviceKey' : serviceKey , 'numOfRows' : '10', 'pageNo' : '1', 'type' : 'xml' }

response = requests.get(url, params=params)
print(response.text)