from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(executable_path="../chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 60)
        self.message = ""


    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"start-text"))).click()

        time.sleep(60)
        self.up = self.driver.find_element(By.CLASS_NAME,'download-speed').text
        self.down = self.driver.find_element(By.CLASS_NAME,'upload-speed').text
    def twitter_login(self,username,password):
        self.driver.get("https://x.com")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span'))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME,"text")))
        self.driver.find_element(By.NAME,"text").send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"css-175oi2r"))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME,"password")))
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"css-175oi2r"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button/div/svg/g/path'))).click()

