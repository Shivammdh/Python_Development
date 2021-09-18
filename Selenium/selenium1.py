from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("https://geeksforgeeks.com")
print(driver.title)
driver.close()
