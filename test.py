from cryptocurrency_bot import CrypoCurrencyBot
from time import sleep

class Tester:
    def __init__(self):
        self.currencies = ["bitcoin", "litecoin", "dogecoin"]
    
    # function to print data
    def print_currencies(self):
        # iterate over this list and get the data currency by currency
        for currency in self.currencies:
            c = CrypoCurrencyBot(currency)
            print(currency + " Value: " + c.get_currency())
            sleep(1)

if __name__ == "__main__":
    t = Tester()
    t.print_currencies()
