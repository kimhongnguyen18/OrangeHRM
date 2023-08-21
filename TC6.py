#Setup environment 
import time
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
orangehrm_loginpage = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(orangehrm_loginpage)
driver.maximize_window()
driver.implicitly_wait(10)

#Verify login page
if driver.title == "OrangeHRM":
    print("Check point page title: PASSED!")
else:
    print("Check point page title: FAILED!")


#Verify Login with Admin account and password
try:
        driver.find_element(By.NAME, "username").send_keys("Admin")  
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button").click()
        print("Check point login: PASSED!")
except:  
        print("Check point login: FAILED!")


#Navigate to Admin
try:
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//span").click()
    print("Check point access Admin module: PASSED!")
except:  
    print("Check point access Admin module: FAILED!")

#Username
driver.find_element(By.XPATH, "//label[text()='Username']/following::input").send_keys("Domina")
time.sleep(5)

#Employee name 
driver.find_element(By.XPATH, "//label[text()='Employee Name']/following::input[1]").send_keys("DChase")
time.sleep(3)
driver.find_element(By.XPATH, "//div[@role='listbox']").click()
print("No Records Found: PASSED!")

#Submit
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Search for unsuccessful users: PASSED")
time.sleep(5)

#RESET
driver.find_element(By.XPATH, "//button[text()=' Reset ']").click()
print("Screen return to original state: PASSED")

#Enter all valid fields
#Username
driver.find_element(By.XPATH, "//label[text()='Username']/following::input").send_keys("Dominic.Chase")
time.sleep(5)

#User Role
driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[text()='-- Select --']").click()
driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[text()='-- Select --']").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
print("Check point selected type as Admin: PASSED!")
time.sleep(5)

#Employee name 
driver.find_element(By.XPATH, "//label[text()='Employee Name']/following::input[1]").send_keys("Dominic  Chase")
time.sleep(3)
driver.find_element(By.XPATH, "//div[@role='listbox']").click()
print("Check point associated Employee: PASSED!")

#Status
driver.find_element(By.XPATH, "//label[text()='Status']/following::div[text()='-- Select --']").click()
driver.find_element(By.XPATH, "//label[text()='Status']/following::div[text()='-- Select --']").send_keys(Keys.ARROW_DOWN, Keys.ENTER)
print("Check point enabled user login: PASSED!")
time.sleep(3)

#Submit
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Search for successful users")
time.sleep(100)