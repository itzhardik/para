import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

#Single web element
login = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
print(login)
login.click()

#Multiple we elements
footer = driver.find_element(By.XPATH, " //div[@class='footer']//a")
print("Footer", footer, footer.text)

try:
    invalid_xpath = driver.find_element(By.XPATH, " //div[@class='footer-xyz']")
    print(invalid_xpath)
except selenium.common.exceptions.NoSuchElementException as e:
    print("No such XPath present: ", e)

print('###### Find Elements #############')

#Single web element
login = driver.find_elements(By.XPATH, "//a[normalize-space()='Log in']")
print(login, len(login))
#login.click()

#Multiple we elements
footer = driver.find_elements(By.XPATH, " //div[@class='footer']//a")
print("Footer", footer, footer[0].text)

try:
    invalid_xpath = driver.find_elements(By.XPATH, " //div[@class='footer-xyz']")
    print(invalid_xpath)
except selenium.common.exceptions.NoSuchElementException as e:
    print("No such XPath present: ", e)

driver.get("https://admin-demo.nopcommerce.com/login")
e_mail_tb = driver.find_element(By.XPATH, "//input[@id='Email']")
print(e_mail_tb.text)
print(e_mail_tb.get_attribute('value'))
e_mail_tb.send_keys("abc.xyz.com")
print('\n', e_mail_tb.get_attribute('value'))

login_bt = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print(login_bt.text)
print(login_bt.get_attribute('class'))
driver.close()