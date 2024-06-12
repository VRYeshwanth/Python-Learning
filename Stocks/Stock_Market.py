from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import json
from datetime import date

def formatted_date():
    d = date.today()
    fd = d.strftime("%d-%m-%Y")
    return fd

def extract_stocks(file):
    try:
        with open(file, "r") as f:
            l = f.readlines()
            l = [i.strip() for i in l]
            return l
    except FileNotFoundError:
        print("No file found")
        exit(0)
pth = r"C:\Users\yeshw\OneDrive\Desktop\Python-Learning\Stocks\Codes.txt"
stock_list = extract_stocks(pth)
data = {}
for stock in stock_list:
    browser = webdriver.Chrome()
    sleep(2)
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={stock}"
    sleep(2)
    browser.get(url)
    browser.maximize_window()
    sleep(1)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    name = soup.find("h2", id="quoteName").text.strip()
    current_price = soup.find("span", id="quoteLtp").text.strip()
    profitorloss = soup.find("span", id="priceInfoStatus").text.strip()
    table = soup.find("table", id="priceInfoTable")
    prices = table.find_all("td")[:5]
    prev_close = prices[0].text.strip()
    open_price = prices[1].text.strip()
    high = prices[2].text.strip()
    low = prices[3].text.strip()
    close_price = prices[4].text.strip()

    data[name] = {
        "Current Price": current_price,
        "Profit/Loss": profitorloss,
        "Previous Close": prev_close,
        "Open": open_price,
        "High": high,
        "Low": low,
        "Close": close_price
    }
    browser.quit()

with open(fr"C:\Users\yeshw\OneDrive\Desktop\Python-Learning\Stocks\Stock Data ({formatted_date()}).json", "w") as f:
    json.dump(data, f, indent=4)