import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
main_win = driver.current_window_handle
print(driver.title)

new_win_1 = driver.find_element(By.XPATH, "//a[normalize-space()='nopCommerce']")
new_win_1.click()

all_cur_win = driver.window_handles
all_cur_win.remove(main_win)
new_win_1 = all_cur_win[0]

driver.switch_to.window(new_win_1)
print(driver.title)
driver.find_element(By.XPATH, "//img[@title='nopCommerce']")

driver.close()