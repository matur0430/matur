from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=www.naver.com")
driver.implicitly_wait(0.5)
while True:
    message=driver.find_element(by=By.ID,value="time_area")
    print(message.text)
    time.sleep(1)
    if message.text=="2024년 04월 02일 13시 57분 00초":
        break
print("시간 종료")
