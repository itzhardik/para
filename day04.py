from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#Self
self_text = driver.find_element(By.XPATH, '//a[contains(text(), "Lemon Tree Hotels")]/self::a').text
print("Self", self_text)

#Parent
parent_text = driver.find_element(By.XPATH, '//a[contains(text(), "Lemon Tree Hotels")]/parent::td').text
print("Parent", parent_text)

#Ancestor
ancestor_text = driver.find_element(By.XPATH, '//a[contains(text(), "Lemon Tree Hotels")]/ancestor::tr').text
print("Ancestor", ancestor_text)

#findelements
find_ele = driver.find_elements(By.XPATH, '//a[contains(text(), "Lemon Tree Hotels")]/ancestor::tr/child::td')
print('find_ele', len(find_ele))

#descendant *
desc_star = driver.find_element(By.XPATH, '//a[contains(text(), "Lemon Tree Hotels")]/ancestor::tr/descendant::td[2]').text
print("Descendant ", desc_star)


driver.close()