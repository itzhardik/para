from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()

all_titles = driver.find_elements(By.CLASS_NAME, "title")
print("Number of titles: ", len(all_titles))
for each_t in all_titles:
    print(each_t)

all_links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links: ", len(all_links))
driver.close()

driver = None

service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://practicetestautomation.com/")

driver.find_element(By.CSS_SELECTOR,"input#form_first_name_7").send_keys("Hardik")
driver.find_element(By.CSS_SELECTOR, "input.mailpoet_text").send_keys("hardik@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

driver.close()