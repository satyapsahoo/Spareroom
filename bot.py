from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "satya.evolfast@gmail.com"
PASSWORD = "Saleshungry123!"


class SpareBot:

    def __init__(self):
        ser = Service("/Users/satyaprakashsahoo/Documents/Chrome Driver/chromedriver")
        self.driver = webdriver.Chrome(service=ser)
        self.listing_id_list = []
        self.ad_url_list = []
        self.free_early_list = []

    def login(self):
        self.driver.get("https://www.spareroom.co.uk/flatshare/?search_id=1180342642&")
        time.sleep(2)
        cookie_element = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_element.click()
        time.sleep(2)
        login_element = self.driver.find_element(By.ID, "loginButtonNav")
        login_element.click()
        user_login = self.driver.find_element(By.NAME, "email")
        user_login.send_keys(USERNAME)
        pass_entry = self.driver.find_element(By.NAME, "password")
        pass_entry.send_keys(PASSWORD)
        pass_entry.send_keys(Keys.ENTER)

    def get_ads_in_page(self):
        self.listing_id_list.clear()
        self.ad_url_list.clear()
        self.free_early_list.clear()
        ad_elements = self.driver.find_elements(By.CLASS_NAME, "listing-result")
        # number_of_ads = len(ad_elements)
        self.listing_id_list = [ad.get_attribute("data-listing-id") for ad in ad_elements]

        for ad in ad_elements:
            ad_url_element = ad.find_element(By.XPATH, "//article/header[1]/a")
            self.ad_url_list.append(ad_url_element.get_attribute("href"))

        for ad in ad_elements:
            free_early_element = ad.find_element(By.XPATH, "//article/footer/span[1]")
            self.free_early_list.append(free_early_element.text)

    def next_page(self):
        next_page_element = self.driver.find_element(By.CSS_SELECTOR, "#paginationNextPageLink")
        next_page_element.click()



