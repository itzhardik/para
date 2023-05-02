from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

exp_title = "Logged In Successfully | Practice Test Automation"
get_title = driver.title

if get_title == exp_title:
    print('Login test passed')
else:
    print('Login failed')

driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a').click()
get_title2 = driver.title
print(get_title2)
if get_title2 == "Test Login | Practice Test Automation":
    print('Logout test passed')
else:
    print('Logout failed')
driver.close()
####################################################################

driver = None
service_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

if driver.title == "Dashboard / nopCommerce administration":
    print("Login Passed")
else:
    print("Login failed")

driver.find_element(By.XPATH,'//*[@id="navbarText"]/ul/li[3]/a').click()

driver.close()
