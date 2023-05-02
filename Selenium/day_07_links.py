import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)

'''
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

#Find all links in a page
all_links = driver.find_elements(By.TAG_NAME,"a")
all_xpath_links = driver.find_elements(By.XPATH, "//a")

print(len(all_links), len(all_xpath_links))
driver.close()
'''

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
for each_l in all_links:
    url = each_l.get_attribute("href")
    response = requests.head(url=url)
    if response.status_code>=400:
        print(f'URL: {url} returns status code: {response.status_code}')

driver.close()