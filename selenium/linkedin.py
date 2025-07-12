from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from api import password, email
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="../chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com")


def check_element_exists(web_driver,by=By.NAME,timeout=5, value=None):
    WebDriverWait(web_driver,timeout).until(EC.presence_of_element_located((by, value)))


check_element_exists(driver,By.XPATH,value="/html/body/nav/div/a[2]")
sign_button = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
sign_button.click()

check_element_exists(driver,By.ID,value="username")
driver.find_element(By.ID, "username").send_keys(email)

check_element_exists(driver,By.ID,value="password")
driver.find_element(By.ID, "password").send_keys(password)

check_element_exists(driver,By.CLASS_NAME,value="login__form_action_container")
driver.find_element(By.CLASS_NAME, 'login__form_action_container ').click()


check_element_exists(driver, By.LINK_TEXT,value="Jobs")
driver.find_element(By.LINK_TEXT,"Jobs").click()

check_element_exists(driver,By.XPATH,timeout=20,value='/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[2]')
area = driver.find_element(By.XPATH,'/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[2]')

ActionChains(driver).move_to_element(area).send_keys("Addis Ababa" + Keys.ENTER).perform()



