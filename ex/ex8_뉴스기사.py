from selenium import webdriver
from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com/")
driver.implicitly_wait(0.5)
query_text="서울 뉴스"
search_box=driver.find_element(by=By.ID,value="query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
find_button=driver.find_element(by=By.CSS_SELECTOR,value=".news_tit")
find_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#contents > div > div.view-contents-wrapper > div.view-headline.view-box > h4")
print(temp_div.text)
time.sleep(10)

