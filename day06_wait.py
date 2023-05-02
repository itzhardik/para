import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors=yes")

driver = webdriver.Chrome(service=serv_obj, options=options)

wait_time = WebDriverWait(driver, 10, poll_frequency= 2, ignored_exceptions=[ElementClickInterceptedException])   #Explicit wait

driver.get("https://10.20.162.35:8443/OAMUI/OAMUI.html")
driver.maximize_window()
driver.implicitly_wait(10) #secs    Implicit wait

user_nm = driver.find_element(By.XPATH, "//input[@id='x-auto-37-input']")
user_nm.send_keys("rest")
#passwd = driver.find_element(By.XPATH, "//input[@id='x-auto-38-input']")
#passwd.send_keys("restpass")
login_bt_wait = wait_time.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
login_bt_wait.click()
#login_bt = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
#login_bt.click()

time.sleep(10)

driver.close()