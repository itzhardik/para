import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
alert_win = driver.switch_to.alert
print(alert_win.text)
alert_win.send_keys("Hello World!!")
alert_win.accept()

time.sleep(5)
driver.close()