from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

Names = []
Prices = []
Ratings = []

for i in range(2):
    url = f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i+1}"
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(2)
    browser.maximize_window()
    soup = BeautifulSoup(browser.page_source, "html.parser")
    sleep(1)
    browser.quit()
    table = soup.find("div", class_ = "DOjaWF gdgoEp")
    rows = table.find_all("div", class_ = "cPHDOP col-12-12")
    l = len(rows)-2
    rows = rows[:l]

    for row in rows:
        name = row.find("div", class_ = "KzDlHZ").text.strip()
        price = row.find("div", class_ = "Nx9bqj _4b5DiR").text.strip()
        rating = row.find("div", class_ = "XQDdHH")
        
        Names.append(name)
        Prices.append(price)
        if rating:
            Ratings.append(rating.text.strip())
        else:
            Ratings.append("-")
    print(f"Page {i+1} scraped")

data = {
    "Name of Product": Names,
    "Price": Prices,
    "Rating": Ratings
}
df = pd.DataFrame(data)
df.to_excel("Laptop Prices.xlsx")