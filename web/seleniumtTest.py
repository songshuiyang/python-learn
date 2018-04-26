from selenium import webdriver

browser = webdriver.Chrome('D:\python\driver\chromedriver.exe')
browser.get("http://www.songshuiyang.com/login.jsp")
username_elem = browser.find_element_by_name("username")
username_elem.send_keys("xiaoli")

password_elem = browser.find_element_by_name("password")
password_elem.send_keys("mima")

browser.find_element_by_xpath("//button[@type='submit']") .click()

print(browser.page_source)