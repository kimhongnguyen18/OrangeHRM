import time
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
orangehrm_loginpage = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
#
driver.get(orangehrm_loginpage)
driver.maximize_window()
driver.implicitly_wait(10)
#Verify login page
if driver.title == "OrangeHRM":
    print("Check point page title: PASSED!")
else:
    print("Check point page title: FAILED!")

#Verify login with Admin account and Pass
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

#User Role
driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[text()='-- Select --']").click()
driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[text()='-- Select --']").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
print("Check point selected type as Admin: PASSED!")
time.sleep(5)

# Final step to create a user login
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Search for successful users")
time.sleep(100)