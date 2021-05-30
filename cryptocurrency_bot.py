##################################################################################
#  scrape coinmarketcap.com to extract crypto currencies current price.
##################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

class CrypoCurrencyBot:
    def __init__(self):
        self.currencies = ["bitcoin", "litecoin", "dogecoin"]

    # function to scrape the data
    def get_currency(self, currency):
        my_url = f'https://coinmarketcap.com/currencies/{currency.lower()}'
        option = Options()
        option.headless = False     # False - show selenium process, True - selenium work in background
        driver = webdriver.Chrome(executable_path="path-to-chromedriver", options=option)
        driver.get(my_url)
        driver.maximize_window()
        
        # get price using selenium
        # coin_price = driver.find_element_by_xpath("//div[contains(@class, 'priceValue___11gHJ')]").text
        # print(coin_price.text)

        # click market button to show coin markets
        # market_btn = driver.find_elements_by_class_name('hh30zs-0')[1]
        # market_btn.click()
        # sleep(2)

        # get page source using pandas and quit driver
        # dataframes[0] - coin price
        # dataframes[1] - market cap
        # dataframes[2] - yesterday data
        # dataframes[3] - weekly data
        # dataframes[4] - circulating data
        dataframes = pd.read_html(driver.page_source)
        coin_price = dataframes[0][1][0]
        
        driver.quit()

        return coin_price
    
    # function to print data
    def print_currencies(self):
        # iterate over this list and get the data currency by currency
        for currency in self.currencies:
           print(currency + " Value: " + self.get_currency(currency))
           sleep(1)


if __name__ == "__main__":
    c = CrypoCurrencyBot()
    # c.get_currency("bitcoin")
    c.print_currencies()
