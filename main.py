import time
import pandas as pd
from bot import SpareBot
from scraper import Scraper

# Create dataframe and csv to store all scrapped information
df = pd.DataFrame({'listing_id': [],
                   'listing_url': [],
                   'free_early': [],
                   'phone_url': [],
                   'phone_number': []
                   })
df.to_csv('spareroom.csv', index=False)

# User Input: Put the url in the line below
# User Input: Put the number of pages to be searched
# spareroom_url = str(input("Enter the spareroom url to be scrapped:"))
number_of_pages = int(input("Enter the number of pages to be scrapped (e.g. 5):"))

# Initiate the Bot and login
spare_bot = SpareBot()
spare_bot.login()

ind = 0
for n in range(number_of_pages):
    spare_bot.get_ads_in_page()
    time.sleep(5)
    for i in range(len(spare_bot.listing_id_list)):
        df["listing_id"][ind] = spare_bot.listing_id_list[i]
        df["listing_url"][ind] = spare_bot.ad_url_list[i]
        df["free_early"][ind] = spare_bot.free_early_list[i]
        df["phone_url"][ind] = ""
        df["phone_number"][ind] = ""
        ind += 1
    spare_bot.next_page()
    time.sleep(2)

df.to_csv('spareroom.csv', index=False)

page_scraper = Scraper()
for n in range(len(df["listing_url"])):
    ad_url = df["listing_url"][n]
    page_scraper.find_phone_url(ad_url)
    # df["phone_url"][n] =

