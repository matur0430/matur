from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
search=input("찾고싶은 영어단어를 검색해보세요! :")
driver=webdriver.Chrome()
driver.get("https://en.dict.naver.com/#/main")
driver.implicitly_wait(0.5)
query_text=search
search_box=driver.find_element(by=By.ID,value="ac_input")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.CLASS_NAME,value="btn_search")
search_button.click()
answer=driver.find_element(by=By.CSS_SELECTOR,value="#searchPage_entry > div > div:nth-child(1) > ul > li:nth-child(1) > p")
print("20307 김해람\n")
print(answer.text)
time.sleep(10)

