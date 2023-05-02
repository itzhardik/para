import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

all_day_cb = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
for each_cb in all_day_cb:
    if each_cb.get_attribute("id") == "saturday" or each_cb.get_attribute("id") == "sunday":
        each_cb.click()

for each_cb in all_day_cb:
    if each_cb.is_selected():
        each_cb.click()

time.sleep(5)

driver.close()