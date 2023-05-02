from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")

#Count number of rows and columns
rows_element = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("No of rows: ", len(rows_element))
heads = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]//th")
print("No of column: ", len(heads))

#Read specific row and column data
spec_val = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]//td")
print(spec_val.text)

java_sub = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[2]//td")
print(java_sub.text)

#print all rows and column
for i in range(2, len(rows_element) + 1):
    for j in range(1, len(heads) + 1):
        print(driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(i) + "]//td[" + str(j) + "]").text)

driver.close()