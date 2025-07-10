from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from api import password, email


service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com")
sign_button = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
sign_button.click()
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, 'login__form_action_container ').click()
driver.find_element(By.LINK_TEXT,"Jobs").click()
driver.find_element(By.CLASS_NAME,"jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-box__ghost-text-input jobs-search-box__text-input--rounded").send_keys("Web developer" + Keys.ENTER)

