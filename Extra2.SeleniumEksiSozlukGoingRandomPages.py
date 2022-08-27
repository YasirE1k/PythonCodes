from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount=1
entries=[]
entryCount=1
while pageCount <=10:
    randomPage=random.randint(1,1290)
    newUrl=url+str(randomPage)
    browser.get(newUrl)

    elements=browser.find_elements(By.CSS_SELECTOR, '.content')
    for element in elements:
        entries.append(element.text)

    time.sleep(3)
    pageCount+=1

for entry in entries:
    print(str(entryCount)+"***********************")
    print(entry)
    entryCount+=1

browser.close()

#browser.get(url)

#time.sleep(5)
"""
elements=browser.find_elements(By.CSS_SELECTOR, '.content')

for element in elements:
    print("****************")
    print(element.text)
"""
browser.close()

