from selenium import webdriver
driver=webdriver.Chrome('C:\Program Files\chromedriver.exe')
driver.get("https://auth.geeksforgeeks.org/user/shivamsharmamdh/practice/")
#driver.maximize_window()
# Approach 1. Scrolldown window by pixal
#driver.execute_script("window.scrollBy(0,1000)","")

# Approach 2. scrolldown page till element is visible
#flag=driver.find_element_by_xpath("//*[@id='languageChart']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

# Approach 3. scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
