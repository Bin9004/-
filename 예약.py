from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used&x=126.9352215&y=37.5588604&bounds=126.8991726%3B37.5445875%3B126.9712704%3B37.5731305")
driver.find_element_by_xpath("/html/body/div[3]/div/div/a").click()

while True:
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/a").click()
        time.sleep(1.15)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[4]/ul/li[1]/div[2]/div[1]/a").click()
        time,sleep(0.7)
    except:
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/a").click()
    finally:
        continue
d







    
