import requests
from bs4 import BeautifulSoup
from requests import Session


USERNAME = "satya.evolfast@gmail.com"
PASSWORD = "Saleshungry123!"

url_w_phone = "https://www.spareroom.co.uk/flatshare/flatshare_detail.pl?flatshare_id=10389844&search_id=1180342642&city_id=&flatshare_type=offered&search_results=%2Fflatshare%2F%3Foffset%3D20%26search_id%3D1180342642%26sort_by%3Dby_day%26mode%3Dlist&"
url_wo_phone = "https://www.spareroom.co.uk/flatshare/flatshare_detail.pl?flatshare_id=15254694&mode=contact&submode=byemail&flatshare_type=offered&search_id=1180342642&search_results=%2Fflatshare%2F%3Foffset%3D20%26search_id%3D1180342642%26sort_by%3Dby_day%26mode%3Dlist&city_id=9&featured=&alert_id=&alert_type=&upgrade_required=1&"

login_url = "https://www.spareroom.co.uk/flatshare/logon.pl?loginfrom_url=" + url_w_phone
print(login_url)


with Session() as s:
    site = s.get(login_url).text
    bs_content = BeautifulSoup(site, "html.parser")
    token = bs_content.find(name="div", class_="auth hidden-overlay").get("data-csrf-token")
    login_data = {"email": USERNAME, "password": PASSWORD, "csrf_token": token}
    login_request = requests.post(login_url, login_data)
    print(login_request)

    response = s.get(url_w_phone).text
    soup = BeautifulSoup(response, "html.parser")
    phone_element = soup.find(name="li", class_="phoneadvertiser")
    phone_url = phone_element.find(name="a").get("href")
    print(phone_url)

    phone_url_response = s.get(phone_url).text
    phone_url_soup = BeautifulSoup(phone_url_response, "html.parser")
    phone_number = soup.find(name="div", class_="contact-phone__phone-button").find("a").get("href")
    phone_number = phone_number.split(":")[-1]
    print(phone_number)




