from selenium import webdriver
import  time

driver = webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #retuens the title of the page
print(driver.current_url) #return current url
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")
time.sleep(5)
driver.close()
