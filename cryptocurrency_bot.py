##################################################################################
#  scrape coinmarketcap.com to extract crypto currencies current price.
##################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import pandas as pd

class CrypoCurrencyBot:
    def __init__(self, currency):
        self.currency = currency
        
    # function to scrape the data
    def get_currency(self):
        my_url = f'https://coinmarketcap.com/currencies/{self.currency.lower()}'
        option = Options()
        option.headless = False     # False - show selenium process, True - selenium work in background
        driver = webdriver.Chrome(executable_path="E:\Programs\chromedriver\chromedriver.exe", options=option)
        driver.get(my_url)
        driver.maximize_window()
        
        # get price using selenium
        coin_price = driver.find_element_by_xpath("//div[contains(@class, 'priceValue___11gHJ')]").text

        # click market button to show coin markets
        # market_btn = driver.find_elements_by_class_name('hh30zs-0')[1]
        # market_btn.click()
        # sleep(2)

        # get page source using pandas and quit driver
        # dataframes = pd.read_html(driver.page_source)
        # coin_price = dataframes[0][1][0]
        
        driver.quit()

        return coin_price
    
