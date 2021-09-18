'''
Take screenshot in two way:

1. save_screenshot("filename")
2. get_screenshot_as_file("file")
'''
from selenium import webdriver
driver=webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("https://auth.geeksforgeeks.org/user/shivamsharmamdh/practice/")
#driver.save_screenshot("D:\python9am\Selenium\ScreenShot\homepage.jpg")
driver.get_screenshot_as_file("D:\python9am\Selenium\ScreenShot\homepage1.jpg")