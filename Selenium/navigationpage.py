from selenium import webdriver
import  time

driver = webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)