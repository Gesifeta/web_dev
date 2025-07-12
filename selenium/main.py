from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import  time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(executable_path="../chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True )
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
# ...
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.TAG_NAME, "button")
# send keys
first_name.send_keys("Gemechu")
last_name.send_keys("Adam")
email.send_keys("adam@gmail.com")
submit.click()



