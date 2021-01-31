from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('D:\python')
wait = WebDriverWait(driver , 10)
userNameValue = 'NguyenCongTest'
passWordValue = '1234567890123'
driver.get('https://www.instagram.com/')
userName = driver.find_element(EC.element_to_be_clickable())