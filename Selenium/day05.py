import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")

#Application command
print(driver.title)
print(driver.current_url)

driver.close()

# Conditional command
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
search_box = driver.find_element(By.ID, "FirstName")
print("Displayed: ", search_box.is_displayed())
print("Enable:", search_box.is_enabled())

male_radio = driver.find_element(By.XPATH, "//*[@id=\"gender-male\"]")
print("Selected: ", male_radio.is_selected())
male_radio.click()
print("After click Selected: ", male_radio.is_selected())

#Navigational Commands

driver.get("https://demo.nopcommerce.com/")
driver.get("https://www.snapdeal.com/")

driver.back()
driver.forward()
driver.refresh()

driver.close()



driver.close()