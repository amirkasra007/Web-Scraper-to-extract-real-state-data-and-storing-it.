from bs4 import BeautifulSoup as bs4
import requests
import numpy as np
import pandas as pd
from d_URLs import all_Urls
from d_URLs import seperate_URLs
from d_URLs import func_urls
from d_URLs import state_to_num
from d_URLs import ads_short
from data_and_time_crawler import df2exl
from addresses_crawler import df2xlxs

state = input("enter the state you want to scrape its data: ")
link = "https://www.zvg-online.net/{}/index.php"

from d_URLs import *
def d_URLs():
    """Implementing the steps in URLs part"""

    num = state_to_num(state)
    all_urls = func_urls(link)
    seperate_Urls = seperate_URLs(link, state)
    ads_shortened  = ads_short(state, link)
    ads_all = all_Urls(state, ads_shortened)
    
from data_and_time_crawler import *
def data_and_time_crawler():
    """Extracting date and time of the real state ads"""

    ads_shortened  = ads_short(state, link)
    data_and_time_data = crawler_date_time(state, ads_shortened)
    dataset, dataset_excel = df2exl(data_and_time_data)
    print(dataset)

from addresses_crawler import *
def addresses_crawler():
    """Scraping Addresses from the website"""

    ads_shortened  = ads_short(state, link)
    addresses = address_crawler(ads_shortened, state)
    dataset, dataset_excel = df2xlxs(addresses)
    print(dataset)

if __name__ == "__main__":
    d_URLs()
    data_and_time_crawler()
    addresses_crawler()


