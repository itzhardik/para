import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

day_dd = driver.find_element(By.XPATH, "//select[@name='DateOfBirthDay']")
month_dd = driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']")
year_dd = driver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']")

select_day = Select(day_dd)
select_month = Select(month_dd)
select_year = Select(year_dd)

select_day.select_by_value("26")
select_month.select_by_visible_text("December")
select_year.select_by_visible_text("1988")

#Get all the option
all_months = select_month.options
for each_m in all_months:
    print(each_m.text)

time.sleep(5)

driver.close()