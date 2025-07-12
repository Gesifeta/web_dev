from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

        self.up_text = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'download-speed')))
        self.up = self.up_text.find_element(By.CLASS_NAME,'download-speed').text

        self.down_text= self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'upload-speed')))
        self.down = self.down_text.find_element(By.CLASS_NAME,'upload-speed').text
