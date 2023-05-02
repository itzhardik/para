import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ops_obj = webdriver.ChromeOptions()
ops_obj.add_argument("--disable-notifications")
serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")

driver = webdriver.Chrome(service=serv_obj, options=ops_obj)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"Alert").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a")
driver.switch_to.default_content()  # go back to main page
#driver.switch_to.parent_frame()    #switch to parent frame in case of nested frame
time.sleep(5)
driver.close()


