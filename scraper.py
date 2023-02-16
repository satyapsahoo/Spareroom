import requests
from bs4 import BeautifulSoup
from bot import SpareBot

class Scraper:

    def __init__(self):
        self.data1 = str()
        self.list1 = []

    def find_phone_url(self, url):
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        phone_element = soup.find(name="i", class_="far fa-phone page-tabs__icon")
        print(phone_element)
        if phone_element:
            advert_options = soup.find_all(name="a", class_="page-tabs__tab ")
            for option in advert_options:
                if option.get("title") == "Phone advertiser":
                    phone_url = option.get("href")
        else:
            phone_url = "Not Found"
        print(phone_url)


    def find_phone(self, url):
        return None
