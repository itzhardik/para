import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()


time.sleep(5)
driver.close()