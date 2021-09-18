from selenium import webdriver

driver=webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("https://www.geeksforgeeks.org/")
driver.find_element_by_id("userProfileId").click()
driver.find_element_by_xpath("//*[@id='luser']").send_keys("shivamsharmamdh@gmail.com")
#driver.find_element_by_class_name("modal-form-input").send_keys("shivamsharmamdh@gmail.com")
#driver.find_element_by_id("password").send_keys("Shivam@0105")
#driver.find_element_by_xpath("//*[@id='Login']/button").click()
#driver.find_element_by_link_text("geeksforgeeks.org/python-programming-language/?ref=shm")
#driver.find_element_by_xpath("//*[@id='hslider']/li[7]/a").click()